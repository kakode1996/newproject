from django.db import models

# Create your models here.


class Dog(models.Model):
    # objects = None
    name = models.CharField(max_length=50,default=None)
    breed = models.CharField(max_length=50,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

