from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *


class ViewSetType(GenericViewSet):
    serializer_class = SerializerTypeIn
    queryset = Type.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data, context=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'status': 'Tipo de pokemon creado'}, status=status.HTTP_200_OK)

    def list(self, request):
        queryset = Type.objects.all()
        serializer = SerializerTypeOut(queryset,many=True)
        return  Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk = None):
        instance = Type.objects.get(pk = pk)
        serializer = self.serializer_class(data=request.data, context=True)
        if serializer.is_valid(raise_exception=True):
            serializer.update(instance, None)
            return Response({"status": "Tipo actualizado"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk = None):
        Type.objects.get(pk=pk).delete()
        return Response({"status": "Se elimino correctamente"}, status = status.HTTP_200_OK)


class ViewSetAttack(GenericViewSet):
    serializer_class = SerializerAttackIn
    queryset = Attack.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data, context=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "Ataque creado"}, status=status.HTTP_200_OK)

    def list(self, request):
        queryset = Attack.objects.all()
        serializer = SerializerAttackOut(queryset, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def update(self, request, pk=None):
        instance = Attack.objects.get(pk=pk)
        serializer = self.serializer_class(data= request.data, context=True)
        if serializer.is_valid(raise_exception=True):
            serializer.update(instance, None)
            return Response({"status": "Usuario actualizado"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        Attack.objects.get(pk = pk).delete()
        return Response({"status": "Se elimino correctamente"}, status = status.HTTP_200_OK)


class ViewSetPokemon(GenericViewSet):
    serializer_class = SerializerPokemonIn
    queryset = Pokemon.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data = request.data, context=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print('____________________________________________')
            print(serializer)
            return Response({"status" : "Pokemon creado con éxito"}, status=status.HTTP_200_OK)

    def list(self, request):
        queryset = Pokemon.objects.all()
        serializer = SerializerPokemonOut(queryset, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def destroy(self, request, pk = None):
        Pokemon.objects.get(pk = pk).delete()
        return Response({"status": "Se elimino correctamente"}, status=status.HTTP_200_OK)


class ViewSetCoachPokemon(GenericViewSet):
    serializer_class = SerializerCoachPokemonIn
    queryset = coachPokemon.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data, context=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "Entrenador creado con éxito"}, status=status.HTTP_200_OK)


    def list(self, request):
        queryset = coachPokemon.objects.all()
        serializer = SerializerCoachPokemonOut(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        instance = coachPokemon.objects.get(pk = pk)
        serializer = self.serializer_class(data=request.data, context=True)
        if serializer.is_valid(raise_exception=True):
            serializer.update(instance, None)
            return Response({"status" : "Usuario actualizado"}, status = status.HTTP_200_OK)

    def destroy(self, request, pk = None):
        coachPokemon.objects.get(pk = pk).delete()
        return Response({"status": "Se elimino correctamente"}, status=status.HTTP_200_OK)

class ViewSetLogin(GenericViewSet):
    serializer_class = SerializerLoginIn
    queryset = ()
    permission_classes = ()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user, token = serializer.doLogin(request)
            return Response({'User': user.namecoach, 'token': token}, status=status.HTTP_200_OK)