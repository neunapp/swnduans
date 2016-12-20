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


@python_2_unicode_compatible
class Location(TimeStampedModel):
    """Django data model Datos de Localizacion"""

    location_id = models.CharField(
        blank=True,
        max_length=100
    )
    name = models.CharField(
        max_length=200
    )
    street = models.CharField(
        blank=True,
        max_length=100
    )
    city = models.CharField(
        blank=True,
        max_length=100
    )
    state = models.CharField(
        blank=True,
        max_length=100
    )
    country_short = models.CharField(
        blank=True,
        max_length=10
    )
    country = models.CharField(
        blank=True,
        max_length=100
    )
    district = models.CharField(
        blank=True,
        max_length=200
    )

    class Meta:
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Category(TimeStampedModel):
    """Modelo Categorias"""

    name = models.CharField('nombre', max_length=100)
    description = models.CharField(blank=True, max_length=200)
    slug = models.SlugField(editable=False, max_length=200)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


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
        super(Category, self).save(*args, **kwargs)


@python_2_unicode_compatible
class KeyWords(TimeStampedModel):
    """Modelo Palabras clave"""

    name = models.CharField('nombre', max_length=100)

    class Meta:
        verbose_name = 'palabra clave'
        verbose_name_plural = 'palabras clave'

    def __str__(self):
        return self.name
