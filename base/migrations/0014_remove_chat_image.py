# Generated by Django 4.0.6 on 2023-03-04 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_ads_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='image',
        ),
    ]
