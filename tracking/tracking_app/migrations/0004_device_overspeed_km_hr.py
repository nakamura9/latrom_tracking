# Generated by Django 2.2.3 on 2019-07-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking_app', '0003_device_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='overspeed_km_hr',
            field=models.FloatField(default=80.0),
        ),
    ]
