from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser


# Create your models here.
class Address(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    addres = models.CharField(max_length=250, verbose_name='Domicilio')

    def __str__(self):
        return self.addres

    class Meta:
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'
        ordering = ['id']


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key= True, editable = False)
    username = models.CharField(max_length=150, verbose_name='Nombre', unique=True)#charfield requiere max_lenngth a diferencia de un text_field
    lastname = models.CharField(max_length=150, verbose_name='Apellido')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True, verbose_name='fecha de registro')
    age = models.PositiveIntegerField(default = 0) #Define POSITIVOS a diferencia de IntegerField que admite numeros
    email = models.CharField(max_length=100, verbose_name='email')
    password=models.CharField(max_length=150, verbose_name='password')
    is_active = models.BooleanField(null=True, blank=True, default=False)

    USERNAME_FIELD = "username"

    #atributo que representa al objeto tipo toString
    def __str__(self):
        return self.username

    #se le colocan propiedaddes a la entidad
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'
        ordering = ['id']



