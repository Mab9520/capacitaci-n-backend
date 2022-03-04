from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import GenericViewSet
from .serializers import *
from rest_framework.response import Response
from rest_framework import status


class ViewSetWorker(GenericViewSet):
    serializer_class = SerializerWorkerIn
    queryset = Worker.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data = request.data, context=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "Usuario creado"}, status = status.HTTP_200_OK)

    def list(self, request):
        queryset = Worker.objects.all()
        serializer = SerializerWorkerOut(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        instance = Worker.objects.get(pk = pk)
        serializer = self.serializer_class(data=request.data, context=True)
        if serializer.is_valid(raise_exception=True):
            serializer.update(instance, None)
            return Response({"status": "El trabajador se actualizó correctamente"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        Worker.objects.get(pk = pk).delete()
        return Response({'status' : 'El trabajador se eliminó correctamente'}, status= status.HTTP_200_OK)


class ViewSetWorkerTypeWork(GenericViewSet):
    serializer_class = SerializerWorkerTypeWorkIn
    queryset = WorkerTypeWork.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data = request.data, context=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "Tipo de trabajo creado"}, status = status.HTTP_200_OK)

    def list(self, request):
        queryset = WorkerTypeWork.objects.all()
        serializer = SerializerWorkerTypeWorkOut(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        instance = WorkerTypeWork.objects.get(pk=pk)
        serializer = self.serializer_class(data=request.data, context=True)
        if serializer.is_valid(raise_exception=True):
            serializer.update(instance, None)
            return Response({"status": "El tipo de trabajador se actualizó correctamente"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        WorkerTypeWork.objects.get(pk=pk).delete()
        return Response({'status' : 'El tipo de trabajo se ha eliminado correctamente'}, status=status.HTTP_200_OK)


#4 Crearemos el viewset del login
class ViewSetLogin(GenericViewSet):
    #La serializer class de la vista sera el serializador de entrada que creamos
    serializer_class = SerializerLoginIn
    queryset = ()

    permission_classes = () #NOs anula la verificacion del token
    #Antes de crear la funcion debemos ir al archivo settings y pegar lo que mando Gera
    #sobre REST_FRAMEWORK
    #5 Creamos la funcion

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user, token = serializer.doLogin(request)
            return Response({'User' : user.workername, 'token' : token}, status=status.HTTP_200_OK)

        #vamos al serializador y creamos la funcion dologin