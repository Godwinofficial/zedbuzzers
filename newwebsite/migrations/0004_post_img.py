# Generated by Django 3.2.5 on 2021-08-06 08:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newwebsite', '0003_alter_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
    ]
