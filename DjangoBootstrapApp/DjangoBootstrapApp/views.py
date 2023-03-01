from django.shortcuts import render

def homePage(request):
    data = {
        'title': range(24)
    }
    return render(request, "index.html", data)    