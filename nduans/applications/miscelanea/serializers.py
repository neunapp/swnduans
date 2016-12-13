# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Location


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
