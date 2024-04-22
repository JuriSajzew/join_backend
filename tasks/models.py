import datetime
from phone_field import PhoneField
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateField(default=datetime.date.today)
    
class Contact(models.Model):
    user = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = phone = PhoneField(blank=True, help_text='Contact phone number')
    