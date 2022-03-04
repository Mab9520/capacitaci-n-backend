from rest_framework import serializers  # importamos de Serializers
from .models import User, Address
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token

class SerializerUserIn(serializers.Serializer):
    # Recibimos los datos de la misma forma en que han sido definidos en los modelos
    username = serializers.CharField()
    lastname = serializers.CharField()
    address_id = serializers.IntegerField()  # Se coloca como en la base de datos en Workbench
    age = serializers.IntegerField()  # Se importan como IntegerField porque serializers no tiene PositiveIntegerField
    email = serializers.CharField()
    password = serializers.CharField()

    # funciones de validacion
    def validate_username(self, username):
        if self.context:
            return username

        query = User.objects.filter(username=username)
        if len(query) > 0:
            raise serializers.ValidationError('Usuario duplicado') # Validacion a nivel de campo
        else:
            return username

    def validate_email(self, email):
        if self.context:
            return email
        query = User.objects.filter(email=email)
        if len(query) > 0:
            raise serializers.ValidationError('Email duplicado')
        else:
            return email

    def save(self):
        instance = User.objects.create(**self.validated_data) # el keyword se identifica con los **
        instance.set_password(self.validated_data.get('password')) #a esa instancia obtengo el string y se cifra
        instance.save()
        # User.objects.create(username = self._validated_data.get('username')) #otra forma de hacer keywords

    def update(self, instance, validate):
        instance.username = self.validated_data.get("username")
        instance.lastname = self.validated_data.get("lastname")
        instance.age = self.validated_data.get("age")
        instance.email = self.validated_data.get("email")
        instance.save()


class SerializerUserOut(serializers.Serializer):# Serialdor de salida
    # Recibimos los datos de la misma forma en que han sido definidos en los modelos
    id = serializers.IntegerField()
    username = serializers.CharField()
    lastname = serializers.CharField()
    address = serializers.SerializerMethodField()  # A traves del metodo le diremos que va a colocar ahi
    age = serializers.IntegerField()  # Se importan como IntegerField porque serializers no tiene PositiveIntegerField
    email = serializers.CharField()
    password = serializers.CharField()

    def get_address(self, obj:address):
        instance = Address.objects.get(pk = obj.address_id)
        serializer = SerializerAddresIn(instance)
        return serializer.data


class SerializerAddresIn(serializers.Serializer):
    id = serializers.IntegerField()
    addres = serializers.CharField()

    def validate_address(self, addres):
        query = Address.objects.filter(addres)
        if len(query) > 0:
            raise serializers.ValidationError('Domicilio duplicado')

    def save(self):
        Address.objects.create(**self.validated_data)

    def update(self, instance, validate):
        instance.addres = self.validated_data.get('addres')
        instance.save()


class SerializerAddressOut(serializers.Serializer):
    id = serializers.IntegerField()
    addres = serializers.CharField()
    user = serializers.SerializerMethodField()

    def get_user(self, obj:user):

        instance = User.objects.filter(address_id = obj.id)
        serializer = SerializerUserIn(instance, many=True)
        return serializer.data
    # Definimos el método get para obtener el usuario


class SerializerLoginIn(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):#validador a nivel atributo
        instance = User.objects.get(username = attrs['username'])# attrs nos da un diccionario
        if check_password(attrs['password'], instance.password): #recibe dos parametros, el objeto de attrs y el campo en la base de datos regresa true o false
            return attrs #si check_password nos envía TRUE retornamos attrs
        else:
            raise serializers.ValidationError('Datos no coinciden')# si manda false mandamos un error


    def doLogin(self, request):
        instance = User.objects.get(username = self.validated_data.get('username'))
        login(request, instance)
        instance.is_active = True #Activamos el login con esta bandera
        instance.save()
        #obtiene o crea son funciones
        token, created = Token.objects.get_or_create(user = instance)
        print('---------------------------------------')
        print(token)
        return instance, token.key


