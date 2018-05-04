from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Location(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    converted_longitude = models.CharField(max_length=30)
    converted_latitude = models.CharField(max_length=30)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('AllerNow_location_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('AllerNow_location_update', args=(self.slug,))


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
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    body_type = models.CharField(max_length=100)
    location = models.CharField(max_length=30)
    price_per_unit = models.PositiveIntegerField()
    unit_size = models.CharField(max_length=2, choices=TIMEUNIT_CHOICES, default=DAILY)
    year = models.CharField(max_length=4)

    # Relationship Fields
    location = models.OneToOneField(
        Location, null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('AllerNow_car_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('AllerNow_car_update', args=(self.slug,))


class Person(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    phone_number = models.TextField(max_length=10)
    postcode = models.CharField(max_length=4)

    # Relationship Fields
    cars = models.ForeignKey(
        Car, null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('AllerNow_person_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('AllerNow_person_update', args=(self.slug,))


