from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from .models import User, Address

# Create your views here.


class ViewSetUser(GenericViewSet):
    serializer_class = SerializerUserIn
    queryset = User.objects.all()
    #permission_classes = () #se anula la validacion del token

    def create(self, request):
        serializer = self.serializer_class(data = request.data, context = False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "Usuario creado"}, status = status.HTTP_200_OK)

    def list(self, request):
        queryset = User.objects.all()
        serializer = SerializerUserOut(queryset, many=True)# many indica que es un arreglo
        return Response(serializer.data, status = status.HTTP_200_OK)

    def update(self, request, pk = None): #pk se refiere al id
        instance = User.objects.get(pk = pk) #nombre_campo = valor por el que se filtra
        serializer = self.serializer_class(data = request.data, context = True)
        if serializer.is_valid(raise_exception=True):
            serializer.update(instance, None)
            return Response({"status" : "Usuario actualizado"}, status = status.HTTP_200_OK)

    def destroy(self, request, pk = None):
        User.objects.get(pk = pk).delete()
        return Response({"status": "Se elimino correctamente"}, status = status.HTTP_200_OK)


class ViewSetAddress(GenericViewSet):
    serializer_class = SerializerAddresIn
    queryset = Address.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status = status.HTTP_200_OK)

    def list(self, request):
        queryset = Address.objects.all()
        serializer = SerializerAddressOut(queryset, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def update(self, request, pk = None):
        instance = Address.objects.get(pk = pk)
        serializer = self.serializer_class(data = request.data, context=True)
        if serializer.is_valid(raise_exception=True):
            serializer.update(instance, None)
            return Response({"status": "La dirección se actualizó correctamente"}, status = status.HTTP_200_OK)


    def destroy(self, request, pk = None):
        Address.objects.get(pk = pk).delete()
        return Response({"status" : "Se eliminó correctamente"}, status = status.HTTP_200_OK)


class ViewSetlogin(GenericViewSet):
    serializer_class = SerializerLoginIn
    queryset = ()
    permission_classes = ()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)#los datos se reciben por medio del request, son los datos que nos envía front
        if serializer.is_valid(raise_exception=True):
            user, token = serializer.doLogin(request)
            return Response({'User' : user.username, 'token' : token}, status=status.HTTP_200_OK)



