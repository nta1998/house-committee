# Generated by Django 4.0.6 on 2023-03-21 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_profile_is_committee'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='building_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.building'),
        ),
    ]
