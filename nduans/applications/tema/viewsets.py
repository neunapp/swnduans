# -*- encoding: utf-8 -*-
from rest_framework import viewsets, generics
from rest_framework.response import Response

#import serializers applications
from applications.users.serializers import UserSerializer
from applications.miscelanea.serializers import LocationSerializer

#import serializers theme
from .serializaers import ThemeListSerializer, AddEspecialistaSerializer

#import models Theme
from .models import Theme, Specialist


class ThemeListViewSet(viewsets.ModelViewSet):
    """ lista Themas Publicados """
    serializer_class = ThemeListSerializer

    def get_queryset(self):
        kword = self.kwargs['kword']
        return Theme.objects.search_theme(kword)


class AddeEspecialistaViewSet(viewsets.ViewSet):
    """
        ViewSet que registra un especialista
    """

    def create(self, request):
        serializado = AddEspecialistaSerializer(data=request.data)
        if serializado.is_valid():
            #creamos el usuario
            usuario_serializado = UserSerializer(
                data=serializado.validated_data['user']
            )
            if usuario_serializado.is_valid():
                usuario = usuario_serializado.save()
                usuario.apelativo = usuario.email
                usuario.is_active = False
                usuario.type_user = '1'
                usuario.save()

                #creamos el location
                location_serilizado = LocationSerializer(
                    data=serializado.validated_data['location']
                )
                #
                if location_serilizado.is_valid():
                    location = location_serilizado.save()
                else:
                    location = None

                #creamos torneo
                especialista = Specialist(
                    user=usuario,
                    location=location,
                    specialty=serializado.validated_data['specialty'],
                    date_birth=serializado.validated_data['date_birth'],
                    description=serializado.validated_data['description'],
                )
                especialista.save()
                res = {'respuesta':'Se Ha Creado el Torneo','id':'0'}
            else:
                res = {'respuesta':'No se Puede Guardar el Usuario','id':'1'}

        else:
            res = {'respuesta':'No se Ha Podido Crear Torneo','id':'1'}
            print serializado.errors

        return Response(res)
