from django.shortcuts import render
from service.models import Service, Testimonials

def homePage(request):
    #c=Testimonials.objects.all().delete()
    serviceData = Service.objects.all()
    testData = Testimonials.objects.all()
    data = {
        'serviceData': serviceData,
        'testData': testData
    }
    return render(request, "index.html", data)    