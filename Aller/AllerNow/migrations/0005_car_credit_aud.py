# Generated by Django 2.0.3 on 2018-05-20 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AllerNow', '0004_auto_20180515_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='credit_aud',
            field=models.PositiveIntegerField(default=100000),
        ),
    ]