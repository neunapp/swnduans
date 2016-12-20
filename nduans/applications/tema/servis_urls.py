# django
from django.conf.urls import include, url

# local
from . import viewsets


urlpatterns = [
    url(r'^api/tema/especialista/save/$',
        viewsets.AddeEspecialistaViewSet.as_view({'post': 'create'}),
        name='api-especialista_add'
    ),
    url(r'^api/tema/save/$',
        viewsets.AddeThemeViewSet.as_view({'post': 'create'}),
        name='api-tema_add'
    ),
    url(
        r'^api/especialista/listar-temas/$',
        viewsets.ThemeSpecialistListViewSet.as_view({'get': 'list'}),
        name='api-tema_listar_especialista'
    ),
    url(
        r'^api/tema/listar/(?P<kword>[-\w]+)/$',
        viewsets.ThemeListViewSet.as_view({'get': 'list'}),
        name='api-tema_listar'
    ),
]
