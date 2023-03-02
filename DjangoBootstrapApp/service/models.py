from django.db import models

class Service(models.Model):
    serviceIcon=models.CharField(max_length=50)
    serviceTitle=models.CharField(max_length=50)
    serviceDesc=models.TextField()