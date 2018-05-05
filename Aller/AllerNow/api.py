from . import models
from . import serializers
from rest_framework import viewsets, permissions


class LocationViewSet(viewsets.ModelViewSet):
    """ViewSet for the Location class"""

    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarViewSet(viewsets.ModelViewSet):
    """ViewSet for the Car class"""

    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
    permission_classes = [permissions.IsAuthenticated]


class PersonViewSet(viewsets.ModelViewSet):
    """ViewSet for the Person class"""

    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Payment class"""

    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]