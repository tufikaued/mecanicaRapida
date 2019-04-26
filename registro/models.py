from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
COLORS = (
    ('red', 'Rojo'),
    ('blue', 'Azul'),
    ('white','Blanco'),
    ('Green','Verde'),
    ('Gray','Gris'),
    ('Yellow','Amarillo'),
    ('Vine','Vino'),
    ('maroon','Marron'),
    ('Olive','Olivo'),
    ('beige','Beige'),
    ('silver','Plata'),
    ('gold','Dorado'),
)

STATUS_SERVICE = (
    ('register','En Registro'),
    ('waiting','En Espera'),
    ('suspended','Suspendido'),
    ('working','Trabajando'),
    ('finish','Completado'),
    ('delivered','Entregado'),
)

class Owner(models.Model):
    """
    Clase para los dueños de los vehiculos
    """

    firstName   = models.CharField(max_length=50, help_text="Nombre del dueño del vehiculo")
    phone       = models.CharField(max_length=50, null=True, blank=True, help_text="Telefono del dueño del vehiculo")
    email       = models.EmailField(null=True, blank=True, help_text="email del dueño del vehiculo")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False, help_text="Fecha de creacion")
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False, help_text="Fecha de actualizacion")
    created_by  = models.ForeignKey(User, null=True, editable=False, related_name='%(class)s_created', on_delete=models.PROTECT)
    modified_by = models.ForeignKey(User, null=True, editable=False, related_name='%(class)s_modified', on_delete=models.PROTECT)

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de Owner
        """
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        representa el objeto Owner
        """
        return "{0}".format(self.firstName)


class BrandCar(models.Model):
    """
    Clase para la marca de los vehiculos
    """
    brandName = models.CharField(max_length=50, help_text="Nombre de Marca de vehiculos")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False, help_text="Fecha de creacion")
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False, help_text="Fecha de actualizacion")

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de BrandCar
        """
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        representa el objeto BrandCar
        """
        return "{0}".format(self.brandName)


class Car(models.Model):
    """
    Clase para los vehiculos
    """
    brandCar       = models.ForeignKey('BrandCar', on_delete=models.PROTECT, null=True, blank=True, default=None, help_text="Marca del vehiculo")
    owner          = models.ForeignKey('Owner',    on_delete=models.PROTECT, null=True, blank=True, default=None, help_text="Dueño del vehiculo")
    colorCar       = models.CharField(max_length=50, choices=COLORS, help_text="Color del vehiculo")
    modelCar       = models.CharField(max_length=50, help_text="Modelo del vehiculo")
    yearCar        = models.PositiveIntegerField(help_text="Año del vehiculo")
    carPlate       = models.CharField(max_length=10, null=True, blank=True, default=None, help_text="Placa del vehiculo")
    kmDailyAverage = models.PositiveIntegerField(null=True, blank=True, default=None, help_text="Promedio Diario en Kilometros")
    kmActual       = models.PositiveIntegerField(null=True, blank=True, default=None, help_text="Kilometraje actual")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False, help_text="Fecha de creacion")
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False, help_text="Fecha de actualizacion")

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de Car
        """
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        representa el objeto Car
        """
        return '{0},{1} {2}, {3}'.format(self.brandCar, self.modelCar, self.yearCar, self.carPlate)


    
class ToRevision(models.Model):
    """
    Clase para las Revisiones
    """
    toRevisionKm   = models.PositiveIntegerField(null=False, blank=False, default=None, editable=True, help_text="Kilometraje a revisar")
    toRevisionDate = models.DateField(null=True, blank=True, default=None, editable=False, help_text="Fecha estimada a revisar")

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de ToRevision
        """
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        representa el objeto ToRevision
        """
        return '{:,}'.format(self.toRevisionKm)


class ServiceCatalog(models.Model):
    """
    Clase para el catalogo de Servicios
    """
    serviceName = models.CharField(max_length=150)
    toRevision  = models.ManyToManyField('ToRevision', null=False, blank=False, help_text="Revisiones programadas")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False, help_text="Fecha de creacion")
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False, help_text="Fecha de actualizacion")

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de ServiceCatalog
        """
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        representa el objeto ServiceCatalog
        """
        return '{0}'.format(self.serviceName)


class RegisterService(models.Model):
    """
    Clase para Registro de Servicios
    """
    carRegister     = models.ForeignKey('Car', on_delete=models.PROTECT, null=True, blank=True, default=None, help_text="Vehiculo Registrado")
    serviceRegister = models.ForeignKey('ServiceCatalog', on_delete=models.PROTECT, null=True, blank=True, default=None, help_text="Servicio Registrado")
    statusRegister  = models.CharField(max_length=50, choices=STATUS_SERVICE, help_text="Estatus del Servicio")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False, help_text="Fecha de registro")
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False, help_text="Fecha de actualizacion")

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = now()
        self.updated_at = now()
        return super().save(*args, **kwargs)
        #return super(RegisterService, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de RegisterService
        """
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        representa el objeto RegisterService
        """
        return '{0} - {1}, {2}'.format(self.dateOfRegister, self.carRegister, self.serviceRegister)
