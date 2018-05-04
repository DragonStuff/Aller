from . import models

from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Location
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'converted_longitude', 
            'converted_latitude', 
        )


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Car
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'body_type', 
            'price_per_unit', 
            'unit_size', 
            'year', 
            'brand', 
            'plate', 
            'state', 
            'registered_owner', 
            'transmission', 
            'condition', 
            'kilometers', 
            'fuel_type', 
            'color', 
            'seats', 
            'doors', 
            'available_from', 
            'available_to', 
            'image_url', 
            'listing_type', 
        )


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = (
            'slug', 
            'created', 
            'last_updated', 
            'first_name', 
            'last_name', 
            'date_of_birth', 
            'phone_number', 
            'postcode', 
            'email', 
            'rating', 
            'address', 
        )

