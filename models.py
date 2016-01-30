from __future__ import unicode_literals

from django.db import models

# Create your models here.


TYPE_CHOICES = (
    ('vsCntrl', 'vsCntrl'),
    ('Other', 'Other'),
)

TEST_TYPE_CHOICES = (
    ('T&L', 'T&L'),
    ('Other', 'Other'),
)

MERCH_GROUP_CHOICES =(
    ('Health Care', 'Health Care'),
    ('Consumables', 'Consumables'),
    ('Beauty/Personal', 'Beauty/Personal'),
    ('General Merchandising', 'General Merchandising'),
)

SUCCESS_METRIC_CHOICES = (
    ('Sales Lift', 'Sales Lift'),
    ('Other', 'Other'),
)

class Test(models.Model):
    test_no	= models.IntegerField(primary_key=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    test_name = models.CharField(max_length=100)
    test_desc = models.CharField(max_length=250)	
    sponsor = models.CharField(max_length=50)
    merch_group = models.CharField(max_length=50, choices=MERCH_GROUP_CHOICES)
    success_metric = models.CharField(max_length=50, choices=SUCCESS_METRIC_CHOICES)
    success_desc = models.CharField(max_length=100)
    success_value	= models.IntegerField(default=0)
    test_type = models.CharField(max_length=50, choices=TEST_TYPE_CHOICES)




class Store(models.Model):
    test_no = models.IntegerField()
    location_id = models.IntegerField()
    test_store = models.BooleanField(default=0)
    pair = models.IntegerField()




class WaveDate(models.Model):
    test_no = models.IntegerField()
    wave_no = models.IntegerField()
    wave_value = models.CharField(max_length=100)
    pre_start = models.DateField()
    pre_end = models.DateField()
    post_start = models.DateField()
    post_end = models.DateField()


class Product(models.Model):
    test_no = models.IntegerField()
    product_no = models.IntegerField()
    product_level_no = models.IntegerField()
    product_tier = models.IntegerField()
    group_no = models.IntegerField()
