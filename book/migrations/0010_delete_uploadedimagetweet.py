# Generated by Django 5.0.3 on 2024-03-24 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_alter_uploadedimagetweet_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadedImageTweet',
        ),
    ]
