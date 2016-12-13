# django
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    View,
    TemplateView,
    CreateView,
    FormView
)

# Autentificacion de usuario
from django.contrib.auth import authenticate, login, logout

#forms
from .forms import LoginForm, UserRegisterForm


class LoginView(FormView):
    '''
        Logeo del usuario
    '''
    template_name = 'users/login.html'
    success_url = '/'
    form_class = LoginForm

    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['email'],
            password = form.cleaned_data['password'],
        )

        if user is not None:
            if user.is_active:
                login(self.request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect(
                    reverse(
                        'users_app:login'
                    )
                )


class LogoutView(View):
    """
    cerrar sesion
    """
    url = '/auth/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:login'
            )
        )


class UserRegisterView(CreateView):
    template_name = 'users/add.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home_app:index')

    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.username = form.cleaned_data['email']
        password = form.cleaned_data['password']
        usuario.set_password(password)
        usuario.is_active = True
        usuario.type_user = '2'
        usuario.save()
        #realizamos login automatico
        user = authenticate(
            username = form.cleaned_data['email'],
            password = form.cleaned_data['password'],
        )

        if user is not None:
            if user.is_active:
                login(self.request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect(
                    reverse(
                        'users_app:login'
                    )
                )

        return super(UserRegisterView, self).form_valid(form)
