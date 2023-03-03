from django.db import models

class Service(models.Model):
    serviceIcon=models.CharField(max_length=50)
    serviceTitle=models.CharField(max_length=50)
    serviceDesc=models.TextField()

class Testimonials(models.Model):
    testDesc = models.TextField()
    testImg = models.FileField(upload_to="testImg/", max_length=250, null=True, default=None)
    testName = models.CharField(max_length=50)
    testCompany = models.CharField(max_length=50)