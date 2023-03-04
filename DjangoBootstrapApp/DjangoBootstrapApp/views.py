from django.shortcuts import render
from service.models import Service, Testimonials, News

def homePage(request):
    #c=Testimonials.objects.all().delete()
    serviceData = Service.objects.all()
    testData = Testimonials.objects.all()
    newsData = News.objects.all()
    
    data = {
        'serviceData': serviceData,
        'testData': testData,
        'newsData': newsData
    }
    return render(request, "index.html", data)    