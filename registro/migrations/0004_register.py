# Generated by Django 2.2 on 2019-04-14 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_auto_20190413_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfRegister', models.DateField(editable=False, help_text='Fecha de Registro')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('statusRegister', models.CharField(choices=[('register', 'En Registro'), ('waiting', 'En Espera'), ('suspended', 'Suspendido'), ('working', 'Trabajando'), ('finish', 'Completado'), ('delivered', 'Entregado')], help_text='Estatus del Servicio', max_length=50)),
                ('carRegister', models.ForeignKey(blank=True, default=None, help_text='Vehiculo Registrado', null=True, on_delete=django.db.models.deletion.PROTECT, to='registro.Car')),
                ('serviceRegister', models.ForeignKey(blank=True, default=None, help_text='Servicio Registrado', null=True, on_delete=django.db.models.deletion.PROTECT, to='registro.ServiceCatalog')),
            ],
        ),
    ]