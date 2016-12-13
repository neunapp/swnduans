# future
from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel

# django
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

#aplicacion miscelanea
from applications.tema.models import Theme, Specialist

#importamos Manager
from .managers import ThemeRatingManager


@python_2_unicode_compatible
class ThemeRating(TimeStampedModel):
    """Modelo Califiacion Tema"""

    theme = models.ForeignKey(Theme)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_normal'
    )
    point = models.PositiveIntegerField()

    objects = ThemeRatingManager()

    class Meta:
        unique_together = ('theme', 'user',)
        verbose_name = 'Calificacion Tema'
        verbose_name_plural = 'Calificaciones de Temas'

    def __str__(self):
        return str(self.theme)


@python_2_unicode_compatible
class SpecialistRating(TimeStampedModel):
    """Modelo Califiacion Especialista"""

    specialist = models.ForeignKey(Specialist)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='usuario_normal'
    )
    point = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Calificacion Especialista'
        verbose_name_plural = 'Calificacione Especialistas'

    def __str__(self):
        return str(self.specialist)
