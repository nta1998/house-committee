# ------import------
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Building(models.Model):
    id = models.AutoField(primary_key=True)
    full_address = models.CharField(max_length=100)
    floors = models.IntegerField()
    vote_active = models.BooleanField(default=False)
    payment_date = models.DateField()
    committee_name = models.CharField(max_length=30)
    committee_apartment = models.IntegerField()
    committee_phone = models.CharField(max_length=11)
    committee_monthly = models.IntegerField()


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    building_id = models.ForeignKey(
        Building, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    apartment = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=100)
    profile_pic = models.ImageField(default='static/profile_pics.png', blank=True)
    is_committee = models.BooleanField(default=False)
    monthly_payment = models.BooleanField(default=False)

class Pool(models.Model):
    id = models.AutoField(primary_key=True)
    building_id = models.ForeignKey(
        Building, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Title = models.CharField(max_length=50)
    Question = models.TextField(max_length=500, blank=True)
    answered = ArrayField(models.CharField(max_length=500), default=list)
    yes = models.IntegerField()
    no = models.IntegerField()


class Ads(models.Model):
    id = models.AutoField(primary_key=True)
    building_id = models.ForeignKey(
        Building, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Content = models.TextField(max_length=500)
    Title = models.CharField(max_length=50)
    Post_time = models.DateField(auto_now_add=True)


class Payment_ads(models.Model):
    id = models.AutoField(primary_key=True)
    building_id = models.ForeignKey(
        Building, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Content = models.TextField(max_length=500)
    Title = models.CharField(max_length=50)
    price = models.IntegerField()
    Post_time = models.DateField(auto_now_add=True)


class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    profile_id = models.OneToOneField(
        Profile, on_delete=models.SET_NULL, null=True)
    building_id = models.ForeignKey(
        Building, on_delete=models.SET_NULL, null=True)
    answered = ArrayField(models.CharField(max_length=500), default=list)
    vote = models.IntegerField()


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    Description = models.TextField(max_length=100)
    category = models.CharField(max_length=30)
    price = models.IntegerField()
    product_pic = models.ImageField(default='/product_pics.png', blank=True)
    profile_id = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True)


class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    profile_id = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True)
    building_id = models.ForeignKey(
        Building, on_delete=models.SET_NULL, null=True)
    send_time = models.DateTimeField(auto_now_add=True)


class Online(models.Model):
    profile_id = models.IntegerField(unique=True)
    fullname = models.CharField(max_length=50)
    building_id = models.IntegerField()
    img = models.TextField()
