# Generated by Django 5.0.3 on 2024-03-24 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_tweet_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedimagetweet',
            name='tweet',
        ),
    ]
