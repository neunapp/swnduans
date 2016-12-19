# future
from __future__ import unicode_literals

# third-party
from datetime import timedelta, datetime
from model_utils.models import TimeStampedModel

# django
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify

#aplicacion miscelanea
from applications.miscelanea.models import (
    Category,
    Location,
    KeyWords,
)

#import managers
from .managers import ThemeManager, SpecialistManager


@python_2_unicode_compatible
class Specialist(TimeStampedModel):
    """Modelo Especialista"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='usuario_especialista'
    )
    location = models.ForeignKey(Location)
    specialty = models.CharField(
        max_length=200
    )
    date_birth = models.DateField(
        'fecha nacimiento',
        blank=True,
        null=True
    )
    description = models.TextField(blank=True)

    objects = SpecialistManager()

    class Meta:
        verbose_name = 'Especialista'
        verbose_name_plural = 'Especialistas'

    def __str__(self):
        return str(self.user)


@python_2_unicode_compatible
class Theme(TimeStampedModel):
    """Modelo Tema"""

    title = models.CharField(
        blank=True,
        max_length=100
    )
    description = models.CharField(
        blank=True,
        max_length=100
    )
    key_words = models.ForeignKey(KeyWords)
    category = models.ForeignKey(Category)
    content = models.TextField()
    date_public = models.DateField(
        'fecha publicacion',
    )
    publicado = models.BooleanField(default=False)
    specialist = models.ForeignKey(Specialist)
    anulate = models.BooleanField(default=False)
    slug = models.SlugField(
        editable=False,
        max_length=200
    )

    objects = ThemeManager()

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # calculamos el total de segundos de la hora actual
            now = datetime.now()
            total_time = timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s %s' % (self.title, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.title, str(seconds))

        self.slug = slugify(slug_unique)
        super(Theme, self).save(*args, **kwargs)
