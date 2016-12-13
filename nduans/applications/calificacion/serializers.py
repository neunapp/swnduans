from rest_framework import serializers

from .models import ThemeRating, SpecialistRating


class ThemeRatingSerializer(serializers.ModelSerializer):
    """Serializa Base calificacion de un tema"""

    class Meta:
        model = ThemeRating
        fields = (
            'theme',
            'point',
        )
