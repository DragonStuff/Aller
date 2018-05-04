import functools
import operator

from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import CarForm, LocationForm, PersonForm
from .models import Car, Location, Person

from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse

# Need to add delete view for Car.
# https://stackoverflow.com/questions/19382664/python-django-delete-current-object

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

class CarSearchListView(CarListView):
    """
    Display a Blog List page filtered by the search query.
    """
    paginate_by = 10

    def get_queryset(self):
        result = super(CarSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                functools.reduce(operator.and_,
                       (Q(name__icontains=q) for q in query_list)) |
                functools.reduce(operator.and_,
                       (Q(location__name__icontains=q) for q in query_list)) |
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
