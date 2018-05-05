from django.contrib import admin
from django import forms
from .models import Location, Car, Person, Payment

class LocationAdminForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = '__all__'


class LocationAdmin(admin.ModelAdmin):
    form = LocationAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'converted_longitude', 'converted_latitude']

admin.site.register(Location, LocationAdmin)


class CarAdminForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'


class CarAdmin(admin.ModelAdmin):
    form = CarAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'body_type', 'price_per_unit', 'unit_size', 'year', 'brand', 'plate', 'state', 'registered_owner', 'transmission', 'condition', 'kilometers', 'fuel_type', 'color', 'seats', 'doors', 'available_from', 'available_to', 'image_url', 'listing_type']

admin.site.register(Car, CarAdmin)


class PersonAdminForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'


class PersonAdmin(admin.ModelAdmin):
    form = PersonAdminForm
    list_display = ['slug', 'created', 'last_updated', 'first_name', 'last_name', 'date_of_birth', 'phone_number', 'postcode', 'email', 'rating', 'address']

admin.site.register(Person, PersonAdmin)

class PaymentAdminForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentAdmin(admin.ModelAdmin):
    form = PaymentAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(Payment, PaymentAdmin)