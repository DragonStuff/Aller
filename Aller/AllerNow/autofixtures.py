from django.conf import settings
from django.db import models as models
from django.db.models import *
from .models import Car
from autofixture import generators, register, AutoFixture

class CarAutoFixture(AutoFixture):
    field_values={
        'name': generators.ChoicesGenerator(values=("Demio", "Rio", "Accent", "Fit", "Fiesta", "Sonic", "Versa", "Mirage")),
        'body_type': generators.ChoicesGenerator(values=("City Cars", "Superminis", "Hatchbacks", "Mini-vps", "MPVs", "Saloon", "Estates", "Four-door Coupes", "Crossovers", "SUVs", "Cabriolet/convertibles")),
        'brand': generators.ChoicesGenerator(values=("BMW", "Ford", "Honda", "Jeep", "Toyota", "Mazda", "Audi" , "Fiat", "Citroen", "Mitsubishi")),
        'color': generators.ChoicesGenerator(values=("Grey", "White", "Black", "Silver", "Red", "Brown", "Blue", "Dark Blue", "Dark Green", "Purple")),
        'condition': generators.ChoicesGenerator(values=("EXCELLENT", "FINE", "VERY GOOD", "GOOD", "OKAY")),
        'fuel_type': generators.ChoicesGenerator(values=("Premium unleaded petrol", "Super unleaded petrol", "Diesel", "LPG Autogas", "Biodiesel", "Bioethanol")),
        'image_url': generators.ChoicesGenerator(values=("http://127.0.0.1:8000/static/images/pic01.jpg", "http://127.0.0.1:8000/static/images/pic02.jpg", "http://127.0.0.1:8000/static/images/pic03.jpg", "http://127.0.0.1:8000/static/images/pic04.jpg", "http://127.0.0.1:8000/static/images/pic05.jpg")), 
        'price_per_unit': generators.ChoicesGenerator(values=(50, 60, 45, 110, 51, 90, 80, 144, 97, 56)),
        'seats': generators.ChoicesGenerator(values=(1, 2, 3, 4)),
        'year': generators.ChoicesGenerator(values=("2001", "2002", "2003", "2015", "2016", "2017", "2018")),
    }

register(Car, CarAutoFixture)

class PersonAutoFixture(AutoFixture):
    field_values={
        'user': AutoFixture.create('auth.User', 1, field_values={'is_superuser': True}),
    }

register(Person, PersonAutoFixture)