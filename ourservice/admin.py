from django.contrib import admin

# Register your models here.
# from ourservice.models import Service
# class ServiceAdmin(admin.ModelAdmin):
#     list_display=('service_title','service_desc','service_read_link')
# admin.site.register(Service,ServiceAdmin)

# Register your models here.
from ourservice.models import Contactform
class ContactAdmin(admin.ModelAdmin):
    list_display=('fullname','email','subject','message')
admin.site.register(Contactform,ContactAdmin)
