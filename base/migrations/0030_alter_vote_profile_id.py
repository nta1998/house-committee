# Generated by Django 4.0.6 on 2023-03-22 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_building_vote_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='profile_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.profile'),
        ),
    ]
