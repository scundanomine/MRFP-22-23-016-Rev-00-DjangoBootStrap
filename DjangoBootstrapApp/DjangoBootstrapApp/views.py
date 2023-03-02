from django.shortcuts import render
from service.models import Service

def homePage(request):
    serviceData = Service.objects.all()
    data = {
        'serviceData': serviceData
    }
    return render(request, "index.html", data)    