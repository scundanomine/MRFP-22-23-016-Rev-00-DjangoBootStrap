from django.contrib import admin
from service.models import Service, Testimonials, News

class ServiceAdmin(admin.ModelAdmin):
    list_display=('serviceIcon', 'serviceTitle', 'serviceDesc')

class TestAdmin(admin.ModelAdmin):
    list_display=('testDesc', 'testImg', 'testName')
    
class NewsAdmin(admin.ModelAdmin):
    list_display=('newsImg', 'newsHead', 'newsDate', 'newsDesc')
    
admin.site.register(Service,ServiceAdmin)
admin.site.register(Testimonials,TestAdmin)
admin.site.register(News,NewsAdmin)