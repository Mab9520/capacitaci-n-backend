from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.

class Type(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    leveltype = models.IntegerField(default=0, verbose_name="Nivel")
    typename = models.CharField(max_length=100, verbose_name="Tipo")

    def __str__(self):
        return self.typename

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']
        db_table = "tipo"


class Attack(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    attackname = models.CharField(max_length=100, verbose_name="Nombre")
    levelattack = models.IntegerField(default=0, verbose_name="Nivel")

    def __str__(self):
        return self.attackname


    class Meta:
        verbose_name = 'Ataque'
        verbose_name_plural = 'Ataques'
        ordering = ['id']
        db_table = 'ataque'

class Pokemon(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    namepokemon = models.CharField(max_length=100, verbose_name="Nombre")
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    attack = models.ForeignKey(Attack, on_delete=models.CASCADE)

    def __str__(self):
        return self.namepokemon

    class Meta:
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemons'
        ordering = ['id']
        db_table = "pokemon"


class coachPokemon(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, editable=False)
    namecoach = models.CharField(max_length=100, verbose_name='Nombre', unique=True)
    lastname =  models.CharField(max_length=100, verbose_name='Apellidos')
    age =  models.IntegerField(default=0, verbose_name="Edad")
    email = models.CharField(max_length=50, verbose_name='Correo')
    password = models.CharField(max_length=150, verbose_name='Contraseña')
    initialPokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    is_active = models.BooleanField(null=True, blank=True, default=False)
    USERNAME_FIELD = 'namecoach'

    def __str__(self):
        return self.namecoach

    class Meta:
        verbose_name = "Entrenador"
        verbose_name_plural = "Entrenadores"
        ordering = ['id']
        db_table = "entrenador"