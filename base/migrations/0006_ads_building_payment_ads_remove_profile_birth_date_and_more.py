# Generated by Django 4.0.6 on 2023-02-21 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_post_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Content', models.TextField(max_length=500)),
                ('Title', models.TextField(max_length=50)),
                ('Post_time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_address', models.CharField(max_length=100)),
                ('floors', models.IntegerField()),
                ('committee_name', models.CharField(max_length=30)),
                ('committee_apartment', models.IntegerField()),
                ('committee_phone', models.CharField(max_length=11)),
                ('committee_monthly', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment_ads',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Content', models.TextField(max_length=500)),
                ('Title', models.TextField(max_length=50)),
                ('price', models.IntegerField()),
                ('Post_time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='apartment',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vote', models.IntegerField()),
                ('profile_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('product_pic', models.ImageField(blank=True, default='/product_pics.png', upload_to='')),
                ('profile_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Question', models.TextField(blank=True, max_length=500)),
                ('yes', models.IntegerField()),
                ('no', models.IntegerField()),
                ('profile_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('send_time', models.DateTimeField(auto_now_add=True)),
                ('building_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.building')),
                ('profile_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='building_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.building'),
        ),
    ]
