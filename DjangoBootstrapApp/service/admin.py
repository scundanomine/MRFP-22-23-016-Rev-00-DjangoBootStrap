from django.contrib import admin
from service.models import Service, Testimonials

class ServiceAdmin(admin.ModelAdmin):
    list_display=('serviceIcon', 'serviceTitle', 'serviceDesc')

class TestAdmin(admin.ModelAdmin):
    list_display=('testDesc', 'testImg', 'testName')
    
admin.site.register(Service,ServiceAdmin)
admin.site.register(Testimonials,TestAdmin)