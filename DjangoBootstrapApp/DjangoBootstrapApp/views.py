from django.shortcuts import render
from service.models import Service, Testimonials, News

def homePage(request):
    #c=Testimonials.objects.all().delete()
    serviceData = Service.objects.all()
    testData = Testimonials.objects.all()
    newsData = News.objects.all()
    sideFooterData = range(5)
    
    data = {
        'serviceData': serviceData,
        'testData': testData,
        'newsData': newsData,
        'sideFooterData': sideFooterData
    }
    return render(request, "index.html", data)    