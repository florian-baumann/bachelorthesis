# Generated by Django 3.1.1 on 2022-02-22 22:13

from django.db import migrations, models
import neighborhoodApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhoodApp', '0009_auto_20220221_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='geohashList',
            field=models.JSONField(default=neighborhoodApp.models.defaultGeohashList),
        ),
    ]
