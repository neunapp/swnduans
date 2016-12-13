# django
from django.conf.urls import include, url

# local
from . import viewsets


urlpatterns = [
    url(
        r'^api/tema/listar/(?P<kword>[-\w]+)/$',
        viewsets.ThemeListViewSet.as_view({'get': 'list'}),
        name='api-tema_listar'
    ),
    url(r'^api/tema/especialista/save/$',
        viewsets.AddeEspecialistaViewSet.as_view({'post': 'create'}),
        name='api-especialista_add'
    ),
]
