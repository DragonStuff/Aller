from . import models

from rest_framework import serializers


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
            'location', 
            'price_per_unit', 
            'unit_size', 
            'year', 
        )


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


