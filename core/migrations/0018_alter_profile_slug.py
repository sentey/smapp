# Generated by Django 4.1.5 on 2023-01-15 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000001D985EB7EB0>', max_length=255),
        ),
    ]
