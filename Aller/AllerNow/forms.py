from django import forms
from .models import Person, Car, Location


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'postcode', 'cars']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'body_type', 'location', 'price_per_unit', 'unit_size', 'year', 'location']


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'converted_longitude', 'converted_latitude']


