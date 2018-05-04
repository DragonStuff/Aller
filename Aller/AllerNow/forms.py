from django import forms
from .models import Location, Car, Person


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'converted_longitude', 'converted_latitude']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'body_type', 'price_per_unit', 'unit_size', 'year', 'brand', 'plate', 'state', 'registered_owner', 'transmission', 'condition', 'kilometers', 'fuel_type', 'color', 'seats', 'doors', 'available_from', 'available_to', 'image_url', 'listing_type', 'location', 'owner', 'is_rented']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'postcode', 'email', 'rating', 'address', 'user']