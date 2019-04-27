from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

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

    owner_name  = models.CharField(max_length=50, help_text="Nombre del dueño del vehiculo")
    phone       = models.CharField(max_length=50, null=True, blank=True, help_text="Telefono del dueño del vehiculo")
    email       = models.EmailField(null=True, blank=True, help_text="email del dueño del vehiculo")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False, help_text="Fecha de creacion")
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False, help_text="Fecha de actualizacion")
    created_by  = models.ForeignKey(User, null=True, editable=False, related_name='%(class)s_created', on_delete=models.PROTECT)
    modified_by = models.ForeignKey(User, null=True, editable=False, related_name='%(class)s_modified', on_delete=models.PROTECT)
    #slug        = models.SlugField(editable=False)

    class Meta:
        verbose_name = 'owner'
        verbose_name_plural = 'owners'

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de Owner
        """
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        representa el objeto Owner
        """
        return "{0}".format(self.owner_name)


class BrandCar(models.Model):
    """
    Clase para la marca de los vehiculos
    """
    brand_name = models.CharField(max_length=50, help_text="Nombre de Marca de vehiculo")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False, help_text="Fecha de creacion")
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False, help_text="Fecha de actualizacion")
    #slug        = models.SlugField(editable=False)

    class Meta:
        verbose_name = 'brandcar'
        verbose_name_plural = 'brandcars'

    def __str__(self):
        """
        representa el objeto BrandCar
        """
        return "{0}".format(self.brand_name)

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de BrandCar
        """
        return reverse('model-detail-view', args=[str(self.id)])



class Car(models.Model):
    """
    Clase para los vehiculos
    """
    brand_car        = models.ForeignKey(BrandCar, on_delete=models.PROTECT, null=True, blank=True, default=None, related_name='brand_cars', related_query_name='brand', help_text="Marca del vehiculo")
    owner            = models.ForeignKey(Owner,    on_delete=models.PROTECT, null=True, blank=True, default=None, related_name='owners', related_query_name='user_owner', help_text="Dueño del vehiculo")
    color_car        = models.CharField(max_length=50, choices=COLORS, help_text="Color del vehiculo")
    model_car        = models.CharField(max_length=50, help_text="Modelo del vehiculo")
    year_car         = models.PositiveIntegerField(help_text="Año del vehiculo")
    car_plate        = models.CharField(max_length=10, null=True, blank=True, default=None, help_text="Placa del vehiculo")
    km_daily_average = models.PositiveIntegerField(null=True, blank=True, default=None, help_text="Promedio Diario en Kilometros")
    km_actual        = models.PositiveIntegerField(null=True, blank=True, default=None, help_text="Kilometraje actual")
    created_at       = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False, help_text="Fecha de creacion")
    updated_at       = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False, help_text="Fecha de actualizacion")
    #slug             = models.SlugField(editable=False)

    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'cars'

    def __str__(self):
        """
        representa el objeto Car
        """
        return '{0},{1} {2}, {3}'.format(self.brand_car, self.model_car, self.year_car, self.car_plate)

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de Car
        """
        return reverse('model-detail-view', args=[str(self.id)])


    
class ToRevision(models.Model):
    """
    Clase para las Revisiones
    """
    to_revision_Km   = models.PositiveIntegerField(null=False, blank=False, default=None, editable=True, help_text="Kilometraje a revisar")
    to_revision_date = models.DateField(null=True, blank=True, default=None, editable=False, help_text="Fecha estimada a revisar")

    class Meta:
        verbose_name = 'torevision'
        verbose_name_plural = 'torevisions'

    def __str__(self):
        """
        representa el objeto ToRevision
        """
        return '{:,}'.format(self.to_revision_Km)

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de ToRevision
        """
        return reverse('model-detail-view', args=[str(self.id)])



class ServiceCatalog(models.Model):
    """
    Clase para el catalogo de Servicios
    """
    service_name = models.CharField(max_length=150)
    to_revision  = models.ManyToManyField(ToRevision, null=False, blank=False, related_name='to_revisions', related_query_name='revision_check', help_text="Revisiones programadas")
    created_at   = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False, help_text="Fecha de creacion")
    updated_at   = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False, help_text="Fecha de actualizacion")
    #slug         = models.SlugField(editable=False)

    class Meta:
        verbose_name = 'servicecatalog'
        verbose_name_plural = 'servicecatalogs'

    def __str__(self):
        """
        representa el objeto ServiceCatalog
        """
        return '{0}'.format(self.service_name)

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de ServiceCatalog
        """
        return reverse('model-detail-view', args=[str(self.id)])



class RegisterService(models.Model):
    """
    Clase para Registro de Servicios
    """
    car_register     = models.ForeignKey(Car, on_delete=models.PROTECT, null=True, blank=True, default=None, related_name='car_registers', related_query_name='register', help_text="Vehiculo Registrado")
    service_register = models.ForeignKey(ServiceCatalog, on_delete=models.PROTECT, null=True, blank=True, related_name='service_registers', related_query_name='service', default=None, help_text="Servicio Registrado")
    status_register  = models.CharField(max_length=50, choices=STATUS_SERVICE, help_text="Estatus del Servicio")
    comment          = models.TextField(null=True, blank=True, help_text='Informacion del servicio')
    created_at       = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False, help_text="Fecha de registro")
    updated_at       = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False, help_text="Fecha de actualizacion")
    #slug             = models.SlugField(editable=False)

    class Meta:
        verbose_name = 'registerservice'
        verbose_name_plural = 'registerservices'

    def __str__(self):
        """
        representa el objeto RegisterService
        """
        return '{0} - {1}, {2}'.format(self.created_at, self.car_register, self.service_register)

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de RegisterService
        """
        return reverse('model-detail-view', args=[str(self.id)])

    #def save(self, *args, **kwargs):
    #    ''' On save, update timestamps '''
    #    if not self.id:
    #        self.slug = slugify(self)
    #    return super().save(*args, **kwargs)

