from django.db import models

# Create your models here.
class Contact(models.Model):
     first_name = models.CharField(max_length =30)
     last_name = models.CharField(max_length =30)
     email= models.EmailField()
     subject = models.CharField(max_length =30)
     message = models.TextField()