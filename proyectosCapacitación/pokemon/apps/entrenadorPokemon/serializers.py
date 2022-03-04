from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token

class SerializerTypeIn(serializers.Serializer):
    #recibir datos como en el modelo
    typename = serializers.CharField()
    leveltype = serializers.IntegerField()

    def validate_typename(self, typename):
        query = Type.objects.filter(typename = typename)
        if len(query) > 0:
            raise serializers.ValidationError("Tipo de pokemon duplicado")
        else:
            return typename

    def save(self):
        instance = Type.objects.create(**self.validated_data)
        instance.save()

    def update(self, instance, validate):
        instance.leveltype= self.validated_data.get('leveltype')
        instance.save()

class SerializerTypeOut(serializers.Serializer):
    #recibimos los campos como en el modelo
    id = serializers.IntegerField()
    typename = serializers.CharField()
    leveltype = serializers.IntegerField()


class SerializerAttackIn(serializers.Serializer):
    #recibimos los datos como en el modelo
    attackname = serializers.CharField()
    levelattack = serializers.IntegerField()

    def validate_attackname(self, attackname):
        query = Attack.objects.filter(attackname = attackname)
        if len(query) > 0:
            raise serializers.ValidationError("Tipo de ataque duplicado")
        else:
            return attackname

    def save(self):
        instance = Attack.objects.create(**self.validated_data)
        instance.save()

    def update(self, instance, validate):
        instance.levelattack = self.validated_data.get('levelattack')
        instance.save()


class SerializerAttackOut(serializers.Serializer):
    #recibimos los campos como en el modelo
    id = serializers.IntegerField()
    attackname = serializers.CharField()
    levelattack = serializers.IntegerField()


class SerializerPokemonIn(serializers.Serializer):
    #recibimos los campos como en el modelo, las llaves foraneas se llaman como en la tabla de bd
    namepokemon = serializers.CharField()
    type_id = serializers.IntegerField()
    attack_id = serializers.IntegerField()

    #preguntar por validadores

    def save(self):
        instance = Pokemon.objects.create(**self.validated_data)
        instance.save()


class SerializerPokemonOut(serializers.Serializer):
    id = serializers.IntegerField()
    namepokemon = serializers.CharField()
    type = serializers.SerializerMethodField()
    attack = serializers.SerializerMethodField()

    def get_type(self, obj:type):
        instance = Type.objects.get(pk = obj.type_id)
        serializer = SerializerTypeIn(instance)
        return serializer.data

    def get_attack(self, obj:attack):
        instance = Attack.objects.get(pk = obj.attack_id)
        serializer = SerializerAttackIn(instance)
        return serializer.data


class SerializerCoachPokemonIn(serializers.Serializer):
    #recibimos los datos como en el modelo
    namecoach = serializers.CharField()
    lastname = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.CharField()
    password = serializers.CharField()
    initialPokemon_id = serializers.IntegerField()

    def save(self):
        instance = coachPokemon.objects.create(**self.validated_data)
        instance.set_password(self.validated_data.get('password'))  # a esa instancia obtengo el string y se cifra
        instance.save()

    def update(self, instance, validate):
        instance.age = self.validated_data.get('age')
        instance.namecoach = self.validated_data.get('namecoach')
        instance.save()


class SerializerCoachPokemonOut(serializers.Serializer):
    #recibimos los datos como en el modelo
    id = serializers.CharField()
    namecoach = serializers.CharField()
    lastname = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.CharField()
    password = serializers.CharField()
    initialPokemon = serializers.SerializerMethodField()

    def get_initialPokemon(self, obj: initialPokemon):
        instance = Pokemon.objects.get(pk = obj.initialPokemon_id)
        serializer = SerializerPokemonIn(instance)
        return serializer.data


class SerializerLoginIn(serializers.Serializer):
    namecoach = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        instance = coachPokemon.objects.get(namecoach = attrs['namecoach'])
        if check_password(attrs['password'], instance.password):
            return attrs
        else:
            raise serializers.ValidationError("Los campos no coinciden")


    def doLogin(self, request):
        instance = coachPokemon.objects.get(namecoach=self.validated_data.get('namecoach'))
        login(request, instance)
        instance.is_active = True
        instance.save()
        token, created = Token.objects.get_or_create(user=instance)
        print('-----------------------------------------')
        print(token)
        print('---------------------------------------')
        return instance, token.key