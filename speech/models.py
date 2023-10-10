from django.db import models
from django.conf import settings



class speech(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, default='Default Author')

    text = models.CharField(max_length= 200,default= "NO TEXT")


# Create your models here.
