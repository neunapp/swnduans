#datetime import
from datetime import datetime

#django import
from django.conf import settings
from django.db import models


class ThemeManager(models.Manager):
    """procedimientos para tabla Tema"""

    def search_theme(self,kword):
        #buscar tema por clave de busqueda
        return self.filter(
            anulate=False,
            publicado=True,
            title__icontains=kword,
        ).order_by('-created')


class SpecialistManager(models.Manager):
    """Procedimientos Para Tabla Especialistas"""

    def list(self):
        return self.all()
