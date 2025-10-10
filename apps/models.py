from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
         return f"{self.email}{self.password}"


class product(models.Model):
     title = models.CharField(max_length=100)
     description = models.CharField(max_length=500)
     img = models.ImageField(upload_to='images/')