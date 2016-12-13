# -*- encoding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate


from django import forms
from .models import User

class LoginForm(forms.Form):
    """
        Form para iniciar sesion
    """
    email = forms.CharField(
        label = 'email',
        max_length = '35',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'email',
                'autofocus': 'autofocus',
            }
        )
    )
    password = forms.CharField(
        label = 'contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'password',
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        print authenticate(username=email)

        if not authenticate(username=email, password=password):
            raise forms.ValidationError('correo o password incorrectos.')
        else:
            return self.cleaned_data


class UserRegisterForm(forms.ModelForm):
    """
        Form para reistrar Usuario
    """
    password = forms.CharField(
        label = 'password',
        max_length = 30,
        required = True,
        widget = forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ingrese contraseña',
            }
        )
    )
    terms = forms.BooleanField(
        label='Acepto Los Terminos y Condiciones',
        required=False,
    )

    class Meta:
        model = User

        fields = [
            'email',
            'first_name',
            'last_name',
            'phone',
        ]
        labels = {
            'email': 'e-mail',
            'first_name':'nombres',
            'last_name': 'apellidos',
            'phone': 'telefono',
        }

        widgets = {
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Correo electronico'
                }
            ),
            'first_name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre',
                }
            ),
            'last_name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Apellidos'
                }
            ),
            'phone':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'numero de celular',
                }
            ),

        }

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 5:
            mensaje = 'Contraseña es muy corta'
            self.add_error('password',mensaje)
        else:
            return password

    def clean_terms(self):
        terms = self.cleaned_data['terms']

        if terms == False:
            mensaje = 'Debe Aceptar Los Terminos y Condiciones'
            self.add_error('terms',mensaje)
        else:
            return terms
