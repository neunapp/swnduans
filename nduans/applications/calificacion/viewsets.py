# -*- encoding: utf-8 -*-
from rest_framework import viewsets, generics
from rest_framework.response import Response

#import serializers theme
from .serializers import ThemeRatingSerializer, SpeciaToplistSerializer

#import models Theme
from .models import ThemeRating, SpecialistRating


class ThemeRatingAddViewSet(viewsets.ViewSet):

    def create(self, request):
        serializado = ThemeRatingSerializer(data=request.data)

        if serializado.is_valid():
            print '*************'
            serializado.save(
                user=self.request.user,
            )
            res = {'id':'0'}
        else:
            res = {'id':'1'}
            print serializado.errors

        return Response(res)


class SpeciaToplistViewSet(viewsets.ModelViewSet):
    """ lista 7 specialistas mas calificadoss"""
    serializer_class = SpeciaToplistSerializer

    def get_queryset(self):
        return SpecialistRating.objects.top_7_specialist()
