# Generated by Django 5.0.3 on 2024-03-28 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0016_profile_background_image_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Location',
            field=models.CharField(blank=True, null=True),
        ),
    ]
