# Generated by Django 4.1.5 on 2023-01-21 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_remove_profile_location_alter_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7f38647186d0>', max_length=255),
        ),
    ]
