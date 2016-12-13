# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """serializador Registrar usuario"""
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone',
            'gender',
        )
