# Generated by Django 2.0.3 on 2018-05-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AllerNow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='is_rented',
            field=models.CharField(max_length=10),
        ),
    ]
