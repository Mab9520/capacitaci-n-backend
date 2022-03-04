from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

class WorkerTypeWork(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    workertype = models.CharField(max_length=50, verbose_name='Tipo')

    def __str__(self):
        return self.workertype

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']
        db_table = 'tipo'


class Worker(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, editable=False)
    workername = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    lastname = models.CharField(max_length=100, verbose_name='Apellidos')
    email = models.CharField(max_length=50, verbose_name='Correo')
    age = models.IntegerField(default=0, verbose_name='Edad')
    address = models.CharField(max_length=150, verbose_name='Direccion')
    password = models.CharField(max_length=150, verbose_name='Contraseña')
    workertype = models.ForeignKey(WorkerTypeWork, on_delete=models.CASCADE)
    is_active = models.BooleanField(null=True, blank=True, default=False)


    USERNAME_FIELD="workername"

    #atributo que representa al objeto tipo toString
    def __str__(self):
        return self.workername

        # se le colocan propiedaddes a la entidad
    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        db_table = 'trabajador'
        ordering = ['id']
