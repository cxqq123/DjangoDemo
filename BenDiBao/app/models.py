from django.db import models
import json

# Create your models here.

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     sex = models.CharField(max_length=30)


class Activity(models.Model):
    cname = models.CharField(max_length=200)
    ctime = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    photo = models.CharField(max_length=200)
    urlLink = models.CharField(max_length=150)

class Test(models.Model):
    name = models.CharField(max_length=20)


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)