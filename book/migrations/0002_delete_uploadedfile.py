# Generated by Django 5.0.3 on 2024-03-24 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadedFile',
        ),
    ]
