import functools
import operator

from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import CarForm, LocationForm, PersonForm, PaymentForm
from .models import Car, Location, Person, Payment

from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse

# Need to add delete view for Car.
# https://stackoverflow.com/questions/19382664/python-django-delete-current-object

class IndexView(ListView):
    template_name = 'AllerNow/index.html'
    context_object_name = 'index'

    def get_queryset(self):
        """Return the last five published polls."""
        return Car.objects.order_by('-available_from')[:5]

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
                functools.reduce(operator.and_,
                       (Q(name__icontains=q) for q in query_list)) |
                functools.reduce(operator.and_,
                       (Q(location__name__icontains=q) for q in query_list)) |
                functools.reduce(operator.and_,
                       (Q(year__icontains=q) for q in query_list)) |
                functools.reduce(operator.and_,
                       (Q(registered_owner__icontains=q) for q in query_list)) |
                functools.reduce(operator.and_,
                       (Q(brand__icontains=q) for q in query_list))
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