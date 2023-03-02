from django.db import models

class Service(models.Model):
    serviceIcon=models.CharField(max_length=50)
    serviceTitle=models.CharField(max_length=50)
    serviceDesc=models.TextField()

class Testimonals(models.Model):
    testDesc = models.CharField(max_length=50)
    testImgUrl = models.CharField(max_length=50)
    testName = models.CharField(max_length=50)