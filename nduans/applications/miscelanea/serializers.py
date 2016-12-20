# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Location, Category, KeyWords


class LocationSerializer(serializers.ModelSerializer):
    """serializador Registrar Location"""
    class Meta:
        model = Location
        fields = (
            'location_id',
            'name',
            'street',
            'city',
            'state',
            'country_short',
            'country',
            'district',
        )


class CategorySerializer(serializers.ModelSerializer):
    """serializador Registrar Category"""
    class Meta:
        model = Category
        fields = (
            'name',
            'description',
        )


class KeyWordsSerializer(serializers.ModelSerializer):
    """serializador Registrar Palabra Clave"""
    class Meta:
        model = KeyWords
        fields = (
            'name',
        )
