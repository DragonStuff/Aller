# Generated by Django 2.0.3 on 2018-05-20 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AllerNow', '0013_auto_20180520_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
