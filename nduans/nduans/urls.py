#main url
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #
    # Python Social Auth URLs
    url('', include('social.apps.django_app.urls', namespace='social')),

    # urls para la aplicacion home
    url(r'^', include('applications.home.urls', namespace="home_app")),
    # urls para la aplicacion miselanea
    url(r'^', include('applications.tema.urls', namespace="tema_app")),
    # urls para aplicacion califiacion
    url(r'^', include('applications.calificacion.urls', namespace="calificacion_app")),
    # urls para aplicacion usuario
    url(r'^', include('applications.users.urls', namespace="users_app")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
