#datetime import
from datetime import datetime

#django function
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
