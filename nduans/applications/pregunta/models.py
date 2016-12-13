# future
from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel

# django
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

#aplicacion miscelanea
from applications.miscelanea.models import Category


@python_2_unicode_compatible
class Question(TimeStampedModel):
    """Modelo Pregunta"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='specialist_user'
    )
    category = models.ForeignKey(Category)
    title = models.CharField(
        'titulo',
        max_length=100
    )
    description = models.TextField()

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

    def __str__(self):
        return str(self.title)
