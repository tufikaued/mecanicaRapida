from django.contrib import admin
from .models import BrandCar, Owner, Car, ToRevision, ServiceCatalog, RegisterService

class BrandCarManager(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at', 'id']
    list_display = ['brand_name', 'created_at','updated_at', 'id',]
    search_fields = ['brand_name']


class CarManager(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at', 'id']
    list_display = ['brand_car', 'owner', 'color_car', 'model_car', 'year_car', 'car_plate', 'km_daily_average', 'km_actual', 'created_at','updated_at', 'id',]
    search_fields = ['color_car', 'model_car', 'year_car', 'car_plate','brand_car__brand_name','owner__owner_name',]
    list_filter = ['color_car', 'model_car', 'year_car', 'car_plate','brand_car__brand_name','owner__owner_name',]


class RegisterServiceManager(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at', 'id']
    list_display = ['car_register', 'service_register', 'status_register', 'created_at', 'updated_at', 'id',]
    search_fields = ['service_register__service_name','car_register__owner__owner_name','car_register__brand_car__brand_name',]
    list_filter = ['service_register__service_name','car_register__owner__owner_name','car_register',]


class OwnerManager(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at', 'id']
    list_display = ['owner_name', 'phone', 'email', 'created_at', 'updated_at', 'id',]
    search_fields = ['owner_name', 'phone', 'email', ]
    list_filter = ['owner_name', 'phone', 'email', ]


class ServiceCatalogManager(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at', 'id']
    search_fields = ['service_name', ]
    


# Register your models here.
admin.site.register(BrandCar, BrandCarManager)
admin.site.register(Owner, OwnerManager)
admin.site.register(Car, CarManager)
admin.site.register(ToRevision)
admin.site.register(ServiceCatalog, ServiceCatalogManager)
admin.site.register(RegisterService, RegisterServiceManager)