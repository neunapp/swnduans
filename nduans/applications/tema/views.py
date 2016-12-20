# -*- coding: utf-8 -*-

# django
from django.views.generic import DetailView, TemplateView

#import modelos tema
from .models import Theme

#import Rating
from applications.calificacion.models import ThemeRating

class ThemeDetailView(DetailView):
    '''
    Vista para mostrar el detalle de un tema.
    '''
    model = Theme
    template_name = 'tema/theme/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ThemeDetailView, self).get_context_data(**kwargs)
        context['promedio'] = ThemeRating.objects.promedio_calificacion(
            self.get_object().pk,
        )['promedio']
        return context


class EspecialistaAddView(TemplateView):
    """vista para agregar un especialista"""
    template_name = 'tema/specialist/perfil/add.html'


class EspecialistaMsjView(TemplateView):
    template_name = 'tema/specialist/perfil/msj.html'


class ThemeListView(TemplateView):
    """lista temas registrados por un especialista"""
    template_name = 'tema/theme/list.html'


class ThemeAddView(TemplateView):
    """vista para crear un nuevo tema"""
    template_name = 'tema/theme/add.html'
