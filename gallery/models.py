from __future__ import unicode_literals
from django.db import models

import datetime as dt


class Location(models.Model):
    name = models.CharField(max_length=100, null=True)

    def save_location(self):
        self.save()

    def location_update(self, cat1):
        self.update(name=Singapore)

    def __str__(self):
        return self.name


class Image(models.Model):
    Name = models.CharField(max_length=40, null=True)
    Description = models.TextField()
    location = models.ForeignKey(Location, null=True)
    category = models.ForeignKey(Category, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def save_Image(self):
        self.save()

    def image_update(self, picnow):
        self.update(Name='picnow')


@classmethod
   def search_by_Name(cls, search_term):
        images = cls.objects.filter(Name__icontains=search_term)
        return images

    @classmethod
    def get_image_by_id(cls, id):

        image = cls.objects.get(id=id)
        return image


class Category(models.Model):
    types = models.CharField(max_length =100, null=True)

    def __str__(self):
        return self.types

    def save_category(self):
        self.save()

    def category_update(self, types):
        self.update(cat1=food)

    @classmethod
    def todays_images(cls):
        today = dt.date.today()
        images = cls.objects.all()
        return images

    @classmethod
    def days_images(cls, date):
        images = cls.objects.filter(pub_date__date=date)
        return images

    def __str__(self):
        return self.Name


# Create your models here.
