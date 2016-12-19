from rest_framework import serializers

#sserilizdor de otras aplicaciones
from applications.miscelanea.serializers import LocationSerializer
from applications.users.serializers import UserSerializer

from .models import Theme, Specialist



class ThemeListSerializer(serializers.ModelSerializer):
    """Serializa Lista de Temas Publciados"""

    category = serializers.CharField(source='category.name')
    specialist = serializers.CharField(source='specialist.user.first_name')
    specialist_image = serializers.ImageField(source='specialist.user.avatar')

    class Meta:
        model = Theme
        fields = (
            'title',
            'description',
            'key_words',
            'category',
            'content',
            'date_public',
            'specialist',
            'slug',
            'specialist_image'
        )


class AddEspecialistaSerializer(serializers.ModelSerializer):
    """serializador para registrar nuevo especialista"""
    user = UserSerializer(required=False)
    location = LocationSerializer(required=False)

    class Meta:
        model = Specialist
        fields = (
            'user',
            'location',
            'specialty',
            'date_birth',
            'description',
        )
