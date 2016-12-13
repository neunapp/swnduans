# django
from django.conf.urls import include, url

# local
from . import views


urlpatterns = [
    #include url de servicios
    url(r'^', include('applications.calificacion.servis_urls', namespace="calificacion_url")),
    #urls para vistas de tema
    # url(
    #     r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$',
    #     views.ThemeDetailView.as_view(),
    #     name='tema-detail'
    # ),
]
