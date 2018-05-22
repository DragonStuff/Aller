from django import forms
from .models import Location, Car, Person, Payment
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User

# User view, update and control.
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'date_of_birth', 'phone_number', 'postcode', 'email', 'address')
        readonly_fields = ('user', 'rating')

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'converted_longitude', 'converted_latitude']


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['name', 'body_type', 'price_per_unit', 'year', 'brand', 'plate', 'state', 'registered_owner', 'transmission', 'condition', 'kilometers', 'fuel_type', 'color', 'seats', 'doors', 'available_from', 'available_to', 'image_url', 'location']
        available_from = forms.DateField(widget=AdminDateWidget())
        available_to = forms.DateField(widget=AdminDateWidget())
        labels = {
            'name': ('Enter a listing name, such as <i>Honda Civic in Wollongong</i>'),
            'body_type': ('Enter a body type, such as <i>Hatchback</i>'),
            'price_per_unit': ('Enter the price per day here, such as <i>30</i>.'),
            'year': ('Enter the car year of make here, such as <i>2010</i>.'),
            'brand': ('Enter the car brand here, such as <i>Honda</i>.'),
            'plate': ("Enter the car's registered plate number here, such as <i>ARD301</i>."),
            'state': ("Enter the car's registered state here, such as <i>NSW</i>."),
            'registered_owner': ('Enter the car registered owner here, such as <i>Abraham Jones</i>.'),
            'transmission': ('Tick the box if the transmission is automatic.'),
            'condition': ("Enter the car's overall condition here, such as <i>'A+'</i>. It is used for insurance purposes."),
            'kilometers': ('Enter the number of kilometers on the odometer, such as <i>21000</i>.'),
            'fuel_type': ('Enter the car fuel type here, such as <i>Unleaded</i>.'),
            'color': ('Enter the car color here, such as <i>Black</i>.'),
            'seats': ('Enter the number of seats in the car here, such as <i>4</i>.'),
            'doors': ('Enter the number of doors on the car here, such as <i>4</i>.'),
            'available_from': ('Enter the date the car is available from, such as <i>2018-05-17</i>.'),
            'available_to': ('Enter the date the car is available to, such as <i>2018-05-20</i>.'),
            'image_url': ('Upload a picture of your car to imgur.com and paste the direct image url here.'),
            'location': ("Select your car's location from below."),
        }
        help_texts = {
            'name': ('Enter your listing name here.'),
            'body_type': ('Enter the car body type here.'),
            'price_per_unit': ('Enter the price per day here.'),
            'year': ('Enter the car year of make here.'),
            'brand': ('Enter the car brand here.'),
            'plate': ("Enter the car's registered plate number here."),
            'state': ("Enter the car's registered state here."),
            'registered_owner': ('Enter the car registered owner here.'),
            'transmission': ('Tick if the transmission is automatic.'),
            'condition': ("Enter the car's condition here. It is used for insurance purposes."),
            'kilometers': ('Enter the number of kilometers on the odometer.'),
            'fuel_type': ('Enter the car brand here.'),
            'color': ('Enter the car color here.'),
            'seats': ('Enter the number of seats here.'),
            'doors': ('Enter the number of doors.'),
            'available_from': ('Enter the date the car is available from here.'),
            'available_to': ('Enter the date the car is available to here.'),
            'image_url': ('Make sure to paste the direct image url here.'),
            'location': ("Select your car's location."),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['personpaying', 'carchoice', 'amount', 'days']
