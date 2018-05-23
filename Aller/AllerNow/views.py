import functools
import operator

from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import CarForm, LocationForm, PersonForm, PaymentForm, UserForm
from .models import Car, Location, Person, Payment
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json

from django.contrib import messages

from django.forms import inlineformset_factory
import datetime
from django.db.models import Avg
from postman.api import pm_write

# Need to add delete view for Car.
# https://stackoverflow.com/questions/19382664/python-django-delete-current-object

# Custom Person exposed through Payment view for Rating
def rate(request, paymentid, rating):
    # Set a payment rating
    paymentrating = Payment.objects.get(id=paymentid)
    paymentrating.rating = rating
    paymentrating.save()

    # Update the user
    p = Payment.objects.filter(carchoice__owner__id=paymentrating.carchoice.owner.id)
    carowner = Person.objects.get(id=paymentrating.carchoice.owner.id)
    print(list(p.aggregate(Avg('rating')).values()))
    carowner.rating = list(p.aggregate(Avg('rating')).values())[0]
    carowner.save()

    return redirect('dashboard')

# Custom Payment view for controlling link between Person and Payment
def create_payment(request, carChoice, days, datefrom, dateto):
    car = Car.objects.get(id=carChoice)
    diff = abs((car.available_from-car.available_to).days)
    if request.method == 'POST':
            payment = Payment(
                amount = (car.price_per_unit * days) + ((car.price_per_unit * days) / 10) + (((car.price_per_unit * days) / 10) * 3),
                days = days,
                personpaying = request.user.person,
                carchoice = car,
                rating = 5,
                datefrom = datefrom,
                dateto = dateto,
            )
            payment.save()
            # We want to disable the listing until the user has confirmed the ride was successful. 
            car.is_rented = "none"
            # Send a message from admin to the successful lister and listee
            pm_write(
                sender=User.objects.all().get(username="admin"),
                recipient=car.owner.user,
                subject="Congratulations, you have successfully rented your car!",
                body='The user ' + request.user.username + ' has rented your car and their payment of $' + str((car.price_per_unit * days) + ((car.price_per_unit * days) / 10) + (((car.price_per_unit * days) / 10) * 3)) + ' has processed successfully. They should contact you shortly. Please note the payment amount does not include our service fee or GST. You will be credited $' + str((((car.price_per_unit * days) - ((((car.price_per_unit * days) + ((car.price_per_unit * days) / 10) + (((car.price_per_unit * days) / 10) * 3))/100)*5.5)) - (car.price_per_unit * days) / 10)) + '. <br><b>PLEASE SEND US A MESSAGE (REPLY) IF YOU WISH TO RELIST THIS BOOKING OR YOU CAN SIMPLY ADD A NEW LISTING.</b><br>Thank you for using Aller Now.',
            )

            pm_write(
                sender=User.objects.all().get(username="admin"),
                recipient=request.user,
                subject="Congratulations, you have successfully rented a car!",
                body='You have rented a car from ' + car.owner.user.username + ' and your payment amount ($' + str((car.price_per_unit * days) + ((car.price_per_unit * days) / 10) + (((car.price_per_unit * days) / 10) * 3)) + ') was processed successfully. you should see a button in your dashboard shortly to contact the owner for pickup and dropoff information. Thank you for using Aller Now.',
            )
            
            car.save()
            car.owner.user.person.credit_aud = car.owner.user.person.credit_aud + (((car.price_per_unit * days) - ((((car.price_per_unit * days) + ((car.price_per_unit * days) / 10) + (((car.price_per_unit * days) / 10) * 3))/100)*5.5)) - (car.price_per_unit * days) / 10)
            request.user.person.credit_aud = request.user.person.credit_aud - ((car.price_per_unit * days) + ((car.price_per_unit * days) / 10))
            request.user.person.save()
            car.owner.user.person.save()
            messages.success(request, ('Your payment was successfully completed!'))
            return redirect('dashboard')
    else:
        paymentf = PaymentForm()
    return render(request, 'AllerNow/payment_car.html', {
        'car': car,
        'payment': paymentf,
        'days': days,
        'remainingCredit': request.user.person.credit_aud - ((car.price_per_unit * days) + ((car.price_per_unit * days) / 10) - (((car.price_per_unit * days) / 10) * 3)),
        'total': ((car.price_per_unit * days) + ((car.price_per_unit * days) / 10) + (((car.price_per_unit * days) / 10) * 3)),
        'gst': ((car.price_per_unit * days) / 10),
        'maxDays': diff,
        'insurance': (((car.price_per_unit * days) / 10) * 3),
        'datefrom': datefrom,
        'dateto': dateto,
    })

# User update
def update_profile(request):
    obj, created = Person.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        person_form = PersonForm(request.POST, instance=request.user.person)
        if user_form.is_valid() and person_form.is_valid():
            user_form.save()
            person_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('dashboard')
        else:
            messages.error(request, _('Please correct the error.'))
    else:
        user_form = UserForm(instance=request.user)
        person_form = PersonForm(instance=request.user.person)
    return render(request, 'AllerNow/dashboard_update.html', {
        'user_form': user_form,
        'person_form': person_form
    })

def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider="auth0")
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture']
    }
    try:
        myCars = Car.objects.filter(owner=request.user.person).values()
    except:
        myCars = ""
    try:
        rentedCars = Payment.objects.filter(personpaying=request.user.person)
    except:
        rentedCars = ""
    
    return render(request, 'AllerNow/dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4),
        'myCars': myCars,
        'rentedCars': rentedCars,
    })


class IndexView(ListView):
    template_name = 'AllerNow/index.html'
    context_object_name = 'index'

    def get_queryset(self):
        """Return the last five published polls."""
        return Car.objects.order_by('-created')[:5]

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['AllerNow_location_list'] = Location.objects.order_by('name')[:5]
        return context 

class LocationListView(ListView):
    model = Location

class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm

class LocationDetailView(DetailView):
    model = Location

class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm

class CarListView(ListView):
    model = Car
    context_object_name = "AllerNow_car_list"
    paginate_by = 10

class CarSearchListView(CarListView):
    """
    Display a Car List page filtered by the search query.
    """
    paginate_by = 10

    def get_queryset(self):
        result = super(CarSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            print(query_list)
            result = result.filter(
                functools.reduce(operator.or_, (Q(name__icontains=q) for q in query_list)) |
                functools.reduce(operator.or_, (Q(location__name__icontains=q) for q in query_list)) |
                functools.reduce(operator.or_, (Q(year__icontains=q) for q in query_list)) |
                functools.reduce(operator.or_, (Q(registered_owner__icontains=q) for q in query_list)) |
                functools.reduce(operator.or_, (Q(brand__icontains=q) for q in query_list))
            )
        return result

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm

class CarDetailView(DetailView):
    model = Car

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm

class PersonListView(ListView):
    model = Person

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm

class PersonDetailView(DetailView):
    model = Person

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm

class PaymentListView(ListView):
    model = Payment


class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm


class PaymentDetailView(DetailView):
    model = Payment


class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm