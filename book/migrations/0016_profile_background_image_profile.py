# Generated by Django 5.0.3 on 2024-03-27 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='background_image_profile',
            field=models.ImageField(blank=True, null=True, upload_to='background_image_profile/'),
        ),
    ]
