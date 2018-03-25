from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Person, Car, Location
from .forms import PersonForm, CarForm, LocationForm


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


class CarListView(ListView):
    model = Car


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm


class CarDetailView(DetailView):
    model = Car


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm


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

