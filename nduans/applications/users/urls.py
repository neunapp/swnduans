# django
from django.conf.urls import include, url

# local
from . import views


urlpatterns = [
    #urls para la aplicacion home
    url(
        r'^entrar/$',
        views.LoginView.as_view(),
        name='login'
    ),
    url(
        r'^salir/$',
        views.LogoutView.as_view(),
        name='logout'
    ),
    url(
        r'^registro/$',
        views.UserRegisterView.as_view(),
        name='registro'
    ),
]
