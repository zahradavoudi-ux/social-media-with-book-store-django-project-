# Generated by Django 5.0.3 on 2024-03-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_uploadedimagetweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimagetweet',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='imagetweet/'),
        ),
    ]
