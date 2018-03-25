from django.contrib import admin
from django import forms
from .models import Person, Car, Location

class PersonAdminForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'


class PersonAdmin(admin.ModelAdmin):
    form = PersonAdminForm
    list_display = ['slug', 'created', 'last_updated', 'first_name', 'last_name', 'date_of_birth', 'phone_number', 'postcode']
    readonly_fields = ['slug', 'created', 'last_updated', 'first_name', 'last_name', 'date_of_birth', 'phone_number', 'postcode']

admin.site.register(Person, PersonAdmin)


class CarAdminForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'


class CarAdmin(admin.ModelAdmin):
    form = CarAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'body_type', 'location', 'price_per_unit', 'unit_size', 'year']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'body_type', 'location', 'price_per_unit', 'unit_size', 'year']

admin.site.register(Car, CarAdmin)


class LocationAdminForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = '__all__'


class LocationAdmin(admin.ModelAdmin):
    form = LocationAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'converted_longitude', 'converted_latitude']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'converted_longitude', 'converted_latitude']

admin.site.register(Location, LocationAdmin)


