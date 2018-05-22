# Generated by Django 2.0.3 on 2018-05-20 10:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AllerNow', '0015_auto_20180520_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
