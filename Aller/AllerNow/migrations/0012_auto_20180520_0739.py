# Generated by Django 2.0.3 on 2018-05-20 07:39

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('AllerNow', '0011_auto_20180520_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='days',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='id'),
        ),
    ]
