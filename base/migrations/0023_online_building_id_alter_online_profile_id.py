# Generated by Django 4.0.6 on 2023-03-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_alter_online_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='online',
            name='building_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='online',
            name='profile_id',
            field=models.IntegerField(unique=True),
        ),
    ]
