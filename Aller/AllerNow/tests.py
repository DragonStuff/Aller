import unittest
from django.urls import reverse
from django.test import Client
from .models import Location, Car, Person
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


def create_location(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["converted_longitude"] = "converted_longitude"
    defaults["converted_latitude"] = "converted_latitude"
    defaults.update(**kwargs)
    return Location.objects.create(**defaults)


def create_car(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["body_type"] = "body_type"
    defaults["price_per_unit"] = "price_per_unit"
    defaults["unit_size"] = "unit_size"
    defaults["year"] = "year"
    defaults["brand"] = "brand"
    defaults["plate"] = "plate"
    defaults["state"] = "state"
    defaults["registered_owner"] = "registered_owner"
    defaults["transmission"] = "transmission"
    defaults["condition"] = "condition"
    defaults["kilometers"] = "kilometers"
    defaults["fuel_type"] = "fuel_type"
    defaults["color"] = "color"
    defaults["seats"] = "seats"
    defaults["doors"] = "doors"
    defaults["available_from"] = "available_from"
    defaults["available_to"] = "available_to"
    defaults["image_url"] = "image_url"
    defaults["listing_type"] = "listing_type"
    defaults.update(**kwargs)
    if "location" not in defaults:
        defaults["location"] = create_location()
    if "owner" not in defaults:
        defaults["owner"] = create_person()
    return Car.objects.create(**defaults)


def create_person(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["first_name"] = "first_name"
    defaults["last_name"] = "last_name"
    defaults["date_of_birth"] = "date_of_birth"
    defaults["phone_number"] = "phone_number"
    defaults["postcode"] = "postcode"
    defaults["email"] = "email"
    defaults["rating"] = "rating"
    defaults["address"] = "address"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return Person.objects.create(**defaults)


class LocationViewTest(unittest.TestCase):
    '''
    Tests for Location
    '''
    def setUp(self):
        self.client = Client()

    def test_list_location(self):
        url = reverse('app_name_location_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_location(self):
        url = reverse('app_name_location_create')
        data = {
            "name": "name",
            "slug": "slug",
            "converted_longitude": "converted_longitude",
            "converted_latitude": "converted_latitude",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_location(self):
        location = create_location()
        url = reverse('app_name_location_detail', args=[location.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_location(self):
        location = create_location()
        data = {
            "name": "name",
            "slug": "slug",
            "converted_longitude": "converted_longitude",
            "converted_latitude": "converted_latitude",
        }
        url = reverse('app_name_location_update', args=[location.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CarViewTest(unittest.TestCase):
    '''
    Tests for Car
    '''
    def setUp(self):
        self.client = Client()

    def test_list_car(self):
        url = reverse('app_name_car_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_car(self):
        url = reverse('app_name_car_create')
        data = {
            "name": "name",
            "slug": "slug",
            "body_type": "body_type",
            "price_per_unit": "price_per_unit",
            "unit_size": "unit_size",
            "year": "year",
            "brand": "brand",
            "plate": "plate",
            "state": "state",
            "registered_owner": "registered_owner",
            "transmission": "transmission",
            "condition": "condition",
            "kilometers": "kilometers",
            "fuel_type": "fuel_type",
            "color": "color",
            "seats": "seats",
            "doors": "doors",
            "available_from": "available_from",
            "available_to": "available_to",
            "image_url": "image_url",
            "listing_type": "listing_type",
            "location": create_location().pk,
            "owner": create_person().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_car(self):
        car = create_car()
        url = reverse('app_name_car_detail', args=[car.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_car(self):
        car = create_car()
        data = {
            "name": "name",
            "slug": "slug",
            "body_type": "body_type",
            "price_per_unit": "price_per_unit",
            "unit_size": "unit_size",
            "year": "year",
            "brand": "brand",
            "plate": "plate",
            "state": "state",
            "registered_owner": "registered_owner",
            "transmission": "transmission",
            "condition": "condition",
            "kilometers": "kilometers",
            "fuel_type": "fuel_type",
            "color": "color",
            "seats": "seats",
            "doors": "doors",
            "available_from": "available_from",
            "available_to": "available_to",
            "image_url": "image_url",
            "listing_type": "listing_type",
            "location": create_location().pk,
            "owner": create_person().pk,
        }
        url = reverse('app_name_car_update', args=[car.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PersonViewTest(unittest.TestCase):
    '''
    Tests for Person
    '''
    def setUp(self):
        self.client = Client()

    def test_list_person(self):
        url = reverse('app_name_person_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_person(self):
        url = reverse('app_name_person_create')
        data = {
            "slug": "slug",
            "first_name": "first_name",
            "last_name": "last_name",
            "date_of_birth": "date_of_birth",
            "phone_number": "phone_number",
            "postcode": "postcode",
            "email": "email",
            "rating": "rating",
            "address": "address",
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_person(self):
        person = create_person()
        url = reverse('app_name_person_detail', args=[person.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_person(self):
        person = create_person()
        data = {
            "slug": "slug",
            "first_name": "first_name",
            "last_name": "last_name",
            "date_of_birth": "date_of_birth",
            "phone_number": "phone_number",
            "postcode": "postcode",
            "email": "email",
            "rating": "rating",
            "address": "address",
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('app_name_person_update', args=[person.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
