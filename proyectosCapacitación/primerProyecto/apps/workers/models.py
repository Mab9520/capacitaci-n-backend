from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
class Work(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    work = models.CharField(max_length=50, verbose_name='Posición')

    def __str__(self):
        return self.work

    class Meta:
        db_table = 'tipoTrabajo'
        verbose_name = 'TipoTrabajo'
        verbose_name_plural = 'TiposTrabajos'
        ordering = ['id']


class Worker(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nameworker = models.CharField(max_length=150, verbose_name='Nombre')
    address = models.CharField(max_length=150, verbose_name="Direccion")
    curp = models.CharField(max_length=20, verbose_name='CURP')
    email = models.CharField(max_length=50, verbose_name='Correo')
    age = models.IntegerField(default=0)
    typeWorker = models.ForeignKey(Work, on_delete=models.CASCADE)

    def __str__(self):
        return self.nameworker

    class Meta:
        db_table = 'trabajador'
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        ordering = ['id']