from django.db import models

# Create your models h
class Shop_Detail(models.Model):
    Shop_Name = models.CharField(max_length=150)
    Shop_address = models.CharField(max_length=150)
    Number = models.CharField(max_length=13)
    
class Product_detail(models.Model):
    item_name = models.CharField(max_length=100)
    item_rate = models.IntegerField(null=False)
