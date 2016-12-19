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


class SpeciaToplistSerializer(serializers.Serializer):
    """serializa la lista de specialista en top 7"""

    specialist__pk = serializers.CharField()
    specialist__user__first_name = serializers.CharField()
    specialist__user__last_name = serializers.CharField()
    specialist__user__avatar = serializers.URLField()
    promedio = serializers.DecimalField(max_digits=10, decimal_places=3)
