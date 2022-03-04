from rest_framework import serializers
from .models import Worker, WorkerTypeWork
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login
from rest_framework.authtoken.models import Token


class SerializerWorkerIn(serializers.Serializer):
    #Datos como estan en el modelo
    workername = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.CharField()
    age = serializers.IntegerField()
    address = serializers.CharField()
    password = serializers.CharField()
    workertype_id = serializers.IntegerField()

    def validate_workername(self, workername):
        if self.context:
            return workername
        query = Worker.objects.filter(workername=workername)
        if len(query) > 0:
            raise serializers.ValidationError('Usuario duplicado')  # Validacion a nivel de campo
        else:
            return workername

    def validate_email(self, email):
        if self.context:
            return email
        query = Worker.objects.filter(email=email)
        if len(query) > 0:
            raise serializers.ValidationError('Email duplicado')
        else:
            return email

    def save(self):
        instance = Worker.objects.create(**self.validated_data) # el keyword se identifica con los **
        instance.set_password(self.validated_data.get('password')) #a esa instancia obtengo el string y se cifra

        instance.save()

    def update(self, instance, validate):
        instance.age = self.validated_data.get("age")
        instance.address = self.validated_data.get("address")
        instance.password = self.validated_data.get("password")
        instance.workertype_id = self.validated_data.get("workertype_id")
        instance.save()


class SerializerWorkerOut(serializers.Serializer):
    id = serializers.IntegerField()
    workername = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.CharField()
    age = serializers.IntegerField()
    address = serializers.CharField()
    password = serializers.CharField()
    workertype = serializers.SerializerMethodField()

    def get_workertype(self, obj:workertype):
        instance = WorkerTypeWork.objects.get(pk = obj.workertype_id)
        serializer = SerializerWorkerTypeWorkIn(instance)
        return serializer.data


class SerializerWorkerTypeWorkIn(serializers.Serializer):
    workertype = serializers.CharField()

    def save(self):
        WorkerTypeWork.objects.create(**self.validated_data)

    def update(self, instance, validate):
        instance.workertype = self.validated_data.get('workertype')
        instance.save()


class SerializerWorkerTypeWorkOut(serializers.Serializer):
    id = serializers.IntegerField()
    workertype = serializers.CharField()
    worker = serializers.SerializerMethodField()

    def get_worker(self, obj: worker):
        instance = Worker.objects.filter(workertype_id = obj.id)
        serializer = SerializerWorkerIn(instance, many=True)
        return serializer.data


#0 Para el login debemos importar de django check_password y login
#1 Creamos clase serializador de entrada para el login
class SerializerLoginIn(serializers.Serializer):
    #datos que se requieren
    workername = serializers.CharField()
    password = serializers.CharField()

    #2 Creamos un validador
    def validate(self, attrs): #attrs nos trae un diccionario
        #creamos la instancia para obtener el workername
        instance = Worker.objects.get(workername = attrs['workername'])
        #verificamos que el password que recibimos haga check con el password de la instancia que obtenemos
        if check_password(attrs['password'], instance.password):
            #Si el check nos da un True se encontro coincidencia
            return attrs
        else:
            #Si no enviamos un error de validacion
            raise serializers.ValidationError('Los datos no coinciden')
            #3 iremos a la vista



    def doLogin(self, request):
        instance = Worker.objects.get(workername = self.validated_data.get('workername'))
        login(request, instance)
        instance.is_active = True
        instance.save()
        token , created = Token.objects.get_or_create(user = instance)
        print('-----------------------------------------')
        print(token)
        print('---------------------------------------')
        return instance, token.key