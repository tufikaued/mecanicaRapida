from django.contrib import admin
from .models import BrandCar, Owner, Car, ToRevision, ServiceCatalog, RegisterService

class BrandCarManager(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at', 'id']
    list_display = ['brandName', 'created_at','updated_at', 'id',]
    search_fields = ['brandName']


class CarManager(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at', 'id']
    list_display = ['brandCar', 'owner', 'colorCar', 'modelCar', 'yearCar', 'carPlate', 'kmDailyAverage', 'kmActual', 'created_at','updated_at', 'id',]
#    search_fields = ['colorCar','yearCar', 'carPlate','brandcar__brandname',]
    search_fields = ['registro_brandcar__brandName',]
    #registro_car__registro_car


class RegisterServiceManager(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at', 'id']
    list_display = ['carRegister', 'serviceRegister', 'statusRegister', 'created_at', 'updated_at', 'id',]
    search_fields = ['serviceRegister',]
    list_filter = ['carRegister']



# Register your models here.
admin.site.register(BrandCar, BrandCarManager)
admin.site.register(Owner)
admin.site.register(Car, CarManager)
admin.site.register(ToRevision)
admin.site.register(ServiceCatalog)
admin.site.register(RegisterService, RegisterServiceManager)