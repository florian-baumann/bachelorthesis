# Generated by Django 3.2.9 on 2022-02-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhoodApp', '0007_alter_users_accuracy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='location',
        ),
        migrations.AddField(
            model_name='users',
            name='latitude',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='users',
            name='longitude',
            field=models.IntegerField(default=0),
        ),
    ]