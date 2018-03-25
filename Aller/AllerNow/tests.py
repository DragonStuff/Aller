import unittest
from django.urls import reverse
from django.test import Client
from .models import Person, Car, Location
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_person(**kwargs):
    defaults = {}
    defaults["first_name"] = "first_name"
    defaults["last_name"] = "last_name"
    defaults["date_of_birth"] = "date_of_birth"
    defaults["phone_number"] = "phone_number"
    defaults["postcode"] = "postcode"
    defaults.update(**kwargs)
    if "cars" not in defaults:
        defaults["cars"] = create_car()
    return Person.objects.create(**defaults)


def create_car(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["body_type"] = "body_type"
    defaults["location"] = "location"
    defaults["price_per_unit"] = "price_per_unit"
    defaults["unit_size"] = "unit_size"
    defaults["year"] = "year"
    defaults.update(**kwargs)
    if "location" not in defaults:
        defaults["location"] = create_car()
    return Car.objects.create(**defaults)


def create_location(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["converted_longitude"] = "converted_longitude"
    defaults["converted_latitude"] = "converted_latitude"
    defaults.update(**kwargs)
    return Location.objects.create(**defaults)


class PersonViewTest(unittest.TestCase):
    '''
    Tests for Person
    '''
    def setUp(self):
        self.client = Client()

    def test_list_person(self):
        url = reverse('AllerNow_person_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_person(self):
        url = reverse('AllerNow_person_create')
        data = {
            "first_name": "first_name",
            "last_name": "last_name",
            "date_of_birth": "date_of_birth",
            "phone_number": "phone_number",
            "postcode": "postcode",
            "cars": create_car().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_person(self):
        person = create_person()
        url = reverse('AllerNow_person_detail', args=[person.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_person(self):
        person = create_person()
        data = {
            "first_name": "first_name",
            "last_name": "last_name",
            "date_of_birth": "date_of_birth",
            "phone_number": "phone_number",
            "postcode": "postcode",
            "cars": create_car().pk,
        }
        url = reverse('AllerNow_person_update', args=[person.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CarViewTest(unittest.TestCase):
    '''
    Tests for Car
    '''
    def setUp(self):
        self.client = Client()

    def test_list_car(self):
        url = reverse('AllerNow_car_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_car(self):
        url = reverse('AllerNow_car_create')
        data = {
            "name": "name",
            "body_type": "body_type",
            "location": "location",
            "price_per_unit": "price_per_unit",
            "unit_size": "unit_size",
            "year": "year",
            "location": create_car().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_car(self):
        car = create_car()
        url = reverse('AllerNow_car_detail', args=[car.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_car(self):
        car = create_car()
        data = {
            "name": "name",
            "body_type": "body_type",
            "location": "location",
            "price_per_unit": "price_per_unit",
            "unit_size": "unit_size",
            "year": "year",
            "location": create_car().pk,
        }
        url = reverse('AllerNow_car_update', args=[car.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LocationViewTest(unittest.TestCase):
    '''
    Tests for Location
    '''
    def setUp(self):
        self.client = Client()

    def test_list_location(self):
        url = reverse('AllerNow_location_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_location(self):
        url = reverse('AllerNow_location_create')
        data = {
            "name": "name",
            "converted_longitude": "converted_longitude",
            "converted_latitude": "converted_latitude",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_location(self):
        location = create_location()
        url = reverse('AllerNow_location_detail', args=[location.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_location(self):
        location = create_location()
        data = {
            "name": "name",
            "converted_longitude": "converted_longitude",
            "converted_latitude": "converted_latitude",
        }
        url = reverse('AllerNow_location_update', args=[location.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


