from django.contrib import admin
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display=('serviceIcon', 'serviceTitle', 'serviceDesc')
    
admin.site.register(Service,ServiceAdmin)