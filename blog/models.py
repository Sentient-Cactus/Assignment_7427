import datetime

import geocoder as geocoder
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from addresses.models import access_token, Address


class Breed(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('breed-detail')

class Dog(models.Model):
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    date_of_birth = models.DateField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, default='Unknown' ,on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name + ' : ' + str(self.owner)
    def age(self):
        dob = self.date_of_birth
        today = datetime.date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age
    def get_absolute_url(self):
        return reverse('home')
    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/media/images/dog-default.jpg"

class Comment(models.Model):
    dog = models.ForeignKey(Dog, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_post = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.dog.name) + ' - ' + str(self.name)

    def get_absolute_url(self):
        return reverse('dog-detail', kwargs={'pk':str(self.dog.id)})

class Activity(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    location = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    join = models.ManyToManyField(User, related_name='blog_activities')

    def total_joins(self):
        return self.join.count()
    def get_absolute_url(self):
        return reverse('activity')

    access_token = 'pk.eyJ1Ijoia21raW0wMSIsImEiOiJja3YyNHZ6aDQzODE4MnJueW8xb2dreHN6In0.E4vmyvWw7zt-OKTZL-9gTw'

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=access_token)
        g = g.latleg  # [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)