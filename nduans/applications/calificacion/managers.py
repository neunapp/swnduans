#datetime import
from datetime import datetime

#functions django models
from django.db.models import Avg

#django import
from django.conf import settings
from django.db import models


class ThemeRatingManager(models.Manager):
    """procedimientos para tabla calificacion tema"""

    def promedio_calificacion(self,theme_pk):
        #calculamos puntuacion promedio Book.objects.all().aggregate(Avg('price'))
        return self.filter(
            theme__pk=theme_pk,
        ).aggregate(promedio=Avg('point'))


class SpecialistRatingManager(models.Manager):
    """procedimientos para tabla calificacion especialistas"""

    def top_7_specialist(self):
        return self.filter(
            specialist__user__is_active=True,
        ).values(
            'specialist__pk',
            'specialist__user__first_name',
            'specialist__user__last_name',
            'specialist__user__avatar',
        ).annotate(
            promedio=Avg('point')
        )[:7]
