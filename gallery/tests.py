

# Create your tests here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from gallery.models import Image,Category,Location

# Create your tests here.
class CategoryTestClass(TestCase):

  def setUp(self):

    self.cat1 = Category(types='food')
  def test_instance(self):
    self.assertTrue(isinstance(self.cat1,Category))
  def test_save_method(self):
        self.cat1.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
  def tearDown(self):

        Category.objects.all().delete()
  def test_category_update(self):
      
        self.cat1.save_category()
        self.cat1 = Category.objects.filter(types = 'travel').update(types = 'food')
        self.new_category= Category.objects.get(types = 'food')
        self.assertEqual(self.new_category.types,'food')

class LocationTestClass(TestCase):
  def setUp(self):

    self.name = Location(name='kenya')
  def test_instance(self):
    self.assertTrue(isinstance(self.name,Location))

  def test_save_method(self):
        self.name.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

  def tearDown(self):
        
        Location.objects.all().delete()

  def test_location_update(self):
      
        self.name.save_location()
        self.location = Location.objects.filter(name = 'kenya').update(name = 'Singapore')
        self.new_location= Location.objects.get(name = 'Singapore')
        self.assertEqual(self.new_location.name,"Singapore")




class ImageTestClass(TestCase):
  def setUp(self):

    self.Name = Image(Name='yumyum')
    self.Description = Image(Description='Good food is therapeutic')
    self.name =Location(name='Kenya').save()
    self.cat1= Category(types='food').save()
    self.new_Image = Image(Name='yumyum',Description='Good food is therapeutic',location=self.name,category=self.cat1)
  def test_instance(self):
    self.assertTrue(isinstance(self.new_Image,Image))

  def test_save_method(self):
        self.new_Image.save_Image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

  def tearDown(self):
        
        Image.objects.all().delete()
  def test_image_update(self):
        
        self.new_Image.save_Image()
        self.newimage = Image.objects.filter(Name= 'yumyum').update(Description ='Best food')
        self.image_updated = Image.objects.filter(Name='yumyum')
        self.assertEqual(self.image_updated.Name,'yumyum')
def test_get_images_today(self):
        today_images = Image.todays_images()
        self.assertTrue(len(today_images)>0)

def test_get_images_by_date(self):
        test_date = '2019-11-20'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        images_by_date = Image.days_images(date)
        self.assertTrue(len(images_by_date) == 0)
