from django.db import models
from django.utils import timezone


class User(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)




class Skills(models.Model):            
    html = models.IntegerField()
    css = models.IntegerField()
    javascript = models.IntegerField()
    python = models.IntegerField()
    django = models.IntegerField()
    iosDevelopment = models.IntegerField()
    androidDevelopment = models.IntegerField()
