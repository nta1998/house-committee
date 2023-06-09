# Generated by Django 4.0.6 on 2023-03-20 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='building_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.building'),
        ),
        migrations.AddField(
            model_name='payment_ads',
            name='building_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.building'),
        ),
        migrations.AddField(
            model_name='pool',
            name='building_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.building'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=models.TextField(max_length=100),
        ),
    ]
