from django.db import models
from django.utils import timezone

# Create your models here.

class SiteUser(models.Model):
    class Meta:
        db_table = 'siteuser'
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    addressLine1 =models.CharField(max_length=500)
    addressLine2 =models.CharField(max_length=500)
    email = models.EmailField(max_length = 255)
    dob =models.DateField()
    city = models.CharField(max_length = 150)
    state = models.CharField(max_length = 150)
    country = models.IntegerField()
    pin=models.CharField(max_length = 20,default="")
    status = models.CharField(max_length=100)
    
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)
    
class Document(models.Model):
    class Meta:
        db_table = 'document'
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)  