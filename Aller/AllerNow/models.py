from django.conf import settings
from django.contrib.auth import models as auth_models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models as models
from django.db.models import *
from django.urls import reverse
from django_extensions.db import fields as extension_fields
from django_extensions.db.fields import AutoSlugField

class Location(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    converted_longitude = CharField(max_length=30)
    converted_latitude = CharField(max_length=30)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('app_name_location_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('app_name_location_update', args=(self.slug,))


class Person(models.Model):

    # Fields
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    date_of_birth = DateField()
    phone_number = models.CharField(max_length=10)
    postcode = CharField(max_length=4)
    email = models.CharField(max_length=30)
    rating = models.PositiveSmallIntegerField()
    address = models.TextField(max_length=100)

    # Relationship Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('app_name_person_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('app_name_person_update', args=(self.slug,))

class Car(models.Model):

    # List eNum
    DAILY = 'DA'
    WEEKLY = 'WE'
    MONTHLY = 'MO'
    YEARLY = 'YR'
    TIMEUNIT_CHOICES = (
        ('DA', 'Daily'),
        ('WE', 'Weekly'),
        ('MO', 'Monthly'),
        ('YR', 'Yearly'),
    )

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    body_type = CharField(max_length=100)
    price_per_unit = PositiveIntegerField()
    unit_size = CharField(max_length=2, choices=TIMEUNIT_CHOICES, default=DAILY)
    year = models.CharField(max_length=4)
    brand = models.CharField(max_length=30)
    plate = models.CharField(max_length=8)
    state = models.CharField(max_length=3)
    registered_owner = models.CharField(max_length=30)
    transmission = models.BooleanField()
    condition = models.CharField(max_length=30)
    kilometers = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    seats = models.PositiveSmallIntegerField()
    doors = models.PositiveSmallIntegerField()
    available_from = models.DateField()
    available_to = models.DateField()
    image_url = models.URLField()
    listing_type = models.CharField(max_length=2)
    is_rented = models.BooleanField()

    # Relationship Fields
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('app_name_car_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('app_name_car_update', args=(self.slug,))
