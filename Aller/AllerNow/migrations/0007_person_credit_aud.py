# Generated by Django 2.0.3 on 2018-05-20 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AllerNow', '0006_remove_car_credit_aud'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='credit_aud',
            field=models.PositiveIntegerField(default=100000),
        ),
    ]
