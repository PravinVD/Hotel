from django.db import models
from ckeditor.fields import RichTextField 
import datetime

# Create your models here.

class staff_detail1(models.Model):
    First_Name = models.CharField(max_length=100,null=False)
    Last_Name = models.CharField(max_length=100,null=False)
    Address = models.CharField(max_length=200,null=False)
    Mobile_No = models.CharField(max_length=13,null=False)
    Create_date = models.DateField()
    Leave_date = models.DateField()
    Last_update_Date = models.DateTimeField(auto_now=True)

class Salary_model(models.Model):
    Emp_No = models.IntegerField()
    Emp_Name = models.CharField(max_length=200,null=False)
    Amount_Paid = models.IntegerField()
    Amount_Paid_Date = models.DateField()

class daily_expense(models.Model):
    Expense_date = models.DateField()
    description = models.TextField()
    Daily_Total = models.IntegerField()
