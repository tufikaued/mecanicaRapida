from django.contrib import admin
from .models import BrandCar, Owner, Car, ToRevision, ServiceCatalog, RegisterService

class RegisterServiceManager(admin.ModelAdmin):
    readonly_fields = ['dateOfRegister']


# Register your models here.
admin.site.register(BrandCar)
admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(ToRevision)
admin.site.register(ServiceCatalog)
admin.site.register(RegisterService,RegisterServiceManager)