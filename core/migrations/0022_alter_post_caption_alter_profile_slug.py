# Generated by Django 4.1.5 on 2023-01-19 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_post_image_alter_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='<django.db.models.query_utils.DeferredAttribute object at 0x00000211BD0E7EB0>', max_length=255),
        ),
    ]
