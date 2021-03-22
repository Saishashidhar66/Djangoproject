from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    car_id = models.IntegerField(null=True)
    customer_need = models.CharField(max_length=100,null=True)
    car_title = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=False)
    message = models.TextField(null = False)
    phone = models.CharField(max_length=20,null=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True,default = datetime.now)
    def __str__(self):
        return self.email
class Contactpage(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null = True)
    phone = models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.name
