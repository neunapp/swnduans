# -*- encoding: utf-8 -*-
from rest_framework import viewsets, generics
from rest_framework.response import Response

from datetime import datetime

#import serializers applications
from applications.users.serializers import UserSerializer
from applications.miscelanea.serializers import (
    LocationSerializer,
    CategorySerializer,
    KeyWordsSerializer,
)

#import serializers theme
from .serializaers import (
    ThemeListSerializer,
    AddEspecialistaSerializer,
    AddThemeSerializer,
)

#import models Theme
from .models import Theme, Specialist

from applications.miscelanea.models import Category


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
                usuario.set_password(usuario.password)
                usuario.is_active = True
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


class ThemeSpecialistListViewSet(viewsets.ModelViewSet):
    """ lista Themas Publicados de un Especialista"""
    serializer_class = ThemeListSerializer

    def get_queryset(self):
        return Theme.objects.themes_by_user(self.request.user)


class AddeThemeViewSet(viewsets.ViewSet):
    """
        ViewSet que registra un nuevo Tema
    """

    def create(self, request):
        serializado = AddThemeSerializer(data=request.data)
        if serializado.is_valid():
            #creamos la Palabra clave
            kword_serializado = KeyWordsSerializer(
                data=serializado.validated_data['key_words']
            )
            if kword_serializado.is_valid():
                kword = kword_serializado.save()

            #creamos la categoria
            # category_serializado = CategorySerializer(
            #     data=serializado.validated_data['category']
            # )
            # category = category_serializado.save()
            category = Category.objects.all()[0]

            #recuperamos sepciaista
            specialist = Specialist.objects.get(
                user=self.request.user,
            )

            #regitramos el tema
            theme = Theme(
                title=serializado.validated_data['title'],
                description=serializado.validated_data['description'],
                key_words=kword,
                category=category,
                content=serializado.validated_data['content'],
                date_public=datetime.now().date(),
                specialist=specialist,
                publicado=serializado.validated_data['publicado'],
            )
            theme.save()

            res = {'respuesta':'Correctamente Guardado','id':'0'}
            print 'Porceso Completado'

        else:
            res = {'respuesta':'No se Ha Podido Crear Torneo','id':'1'}
            print serializado.errors

        return Response(res)
