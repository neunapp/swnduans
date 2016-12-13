# django
from django.conf.urls import include, url

# local
from . import views


urlpatterns = [
    #urls para vistas de tema
    url(
        r'^especialista/agregar-nuevo/$',
        views.EspecialistaAddView.as_view(),
        name='especialista-add'
    ),
    url(
        r'^mensaje-confirmacion/$',
        views.EspecialistaMsjView.as_view(),
        name='especialista-msj'
    ),
    url(
        r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$',
        views.ThemeDetailView.as_view(),
        name='tema-detail'
    ),

    #include url de servicios
    url(r'^', include('applications.tema.servis_urls', namespace="tema_url")),
]
