from django import forms
from .models import Location, Car, Person, Payment
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User

#Ada
class CreditCardField(forms.CharField):
  def get_cc_type(self, number):
    """
    Gets credit card type given number. Based on values from Wikipedia page
    "Credit card number".
    <a href="http://en.wikipedia.org/w/index.php?title=Credit_card_number
">http://en.wikipedia.org/w/index.php?title=Credit_card_number
</a>    """
    number = str(number)
    #group checking by ascending length of number
    if len(number) == 13:
      if number[0] == "4":
        return "Visa"
    elif len(number) == 14:
      if number[:2] == "36":
        return "MasterCard"
    elif len(number) == 15:
      if number[:2] in ("34", "37"):
        return "American Express"
    elif len(number) == 16:
      if number[:4] == "6011":
        return "Discover"
      if number[:2] in ("51", "52", "53", "54", "55"):
        return "MasterCard"
      if number[0] == "4":
        return "Visa"
    return "Unknown"
 
  def clean(self, value):
    """Check if given CC number is valid and one of the
    card types we accept"""
    if value and (len(value) < 13 or len(value) > 16):
      raise forms.ValidationError("Please enter in a valid "+\
          "credit card number.")
    elif self.get_cc_type(value) not in ("Visa", "MasterCard",
        "American Express", "Discover"):
 
      raise forms.ValidationError("Please enter in a Visa, "+\
          "Master Card, Discover, or American Express credit card number.")
 
    return super(CreditCardField, self).clean(value)

# User view, update and control.
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class PersonForm(forms.ModelForm):
    paycardnumber = CreditCardField(required = True, label = "Card Number")
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'date_of_birth', 'phone_number', 'postcode', 'email', 'address', 'paycardnumber', 'paycardname', 'paycardexpiry')
        readonly_fields = ('user', 'rating')

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'converted_longitude', 'converted_latitude']


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['name', 'body_type', 'price_per_unit', 'year', 'brand', 'plate', 'state', 'registered_owner', 'transmission', 'condition', 'kilometers', 'fuel_type', 'color', 'seats', 'doors', 'available_from', 'available_to', 'image_url', 'location', 'owner']
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
