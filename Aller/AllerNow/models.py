from django.conf import settings
from django.contrib.auth import models as auth_models
from django.contrib.auth import get_user_model

# Authentication controller
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.signals import request_finished

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models as models
from django.db.models import *
from django.urls import reverse
from django_extensions.db import fields as extension_fields
from django_extensions.db.fields import AutoSlugField
import datetime
from django.utils import timezone
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

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

    def __str__(self):
        return u'%s' % (self.name,)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('AllerNow_location_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('AllerNow_location_update', args=(self.slug,))


class Person(models.Model):

    # Fields
    slug = AutoSlugField(populate_from='user__username', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    first_name = CharField(max_length=30, blank=True)
    last_name = CharField(max_length=30, blank=True)
    date_of_birth = DateField(default=timezone.now)
    phone_number = models.CharField(max_length=10, blank=True)
    postcode = CharField(max_length=4, blank=True)
    email = models.CharField(max_length=30, blank=True)
    rating = models.PositiveSmallIntegerField(default=3)
    address = models.TextField(max_length=100, blank=True)

    # Payment
    paycardnumber = models.CharField(max_length=30, blank=True)
    paycardname = models.CharField(max_length=30, blank=True)
    paycardexpiry = models.TextField(max_length=5, blank=True)

    # Credit
    credit_aud = PositiveIntegerField(default=100000)

    # Relationship Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('AllerNow_person_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('AllerNow_person_update', args=(self.slug,))

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
    available_from = models.DateField(default=datetime.date.today)
    available_to = models.DateField()
    image_url = models.URLField()
    listing_type = models.CharField(max_length=2)
    is_rented = models.CharField(max_length=10)

    # Relationship Fields
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % (self.name,)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('AllerNow_car_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('AllerNow_car_update', args=(self.slug,))

class Payment(models.Model):

    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = extension_fields.AutoSlugField(populate_from='id', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    amount = PositiveIntegerField()
    days = PositiveIntegerField()

    # Relationship Fields
    personpaying = models.ForeignKey(Person, on_delete=models.CASCADE)
    carchoice = models.OneToOneField(Car, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(blank=True, validators=[MaxValueValidator(10), MinValueValidator(1)])

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('app_name_payment_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('app_name_payment_update', args=(self.slug,))