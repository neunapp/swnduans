# django
from django.conf.urls import include, url

# local
from . import viewsets


urlpatterns = [
    url(
        r'^api/calificar/tema/add$',
        viewsets.ThemeRatingAddViewSet.as_view({'post': 'create'}),
        name='api-calificar_tema_add'
    ),
]
