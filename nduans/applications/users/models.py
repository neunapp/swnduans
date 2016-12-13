from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):

        email = self.normalize_email(email)
        if not email:
            raise ValueError("el email es obligatorio")

        user = self.model(
            email=email,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    TYPE_CHOICES = (
        ('0', 'Admin'),
        ('1', 'Especialista'),
        ('2', 'Normal'),
    )
    apelativo = models.CharField('apelativo', max_length=50)
    email = models.EmailField('correo electronico', unique=True)
    first_name = models.CharField('nombres', max_length=50)
    last_name = models.CharField('apellidos', max_length=50)
    avatar = models.ImageField(upload_to='users', blank=True, null=True)
    phone = models.CharField('telefono', max_length=50, blank=True, null=True)
    gender = models.CharField('sexo', max_length=1, choices=GENDER_CHOICES)
    type_user = models.CharField('tipo de usuario', max_length=2, choices=TYPE_CHOICES, null=True, blank=True)

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return "%s %s" % (self.last_name, self.first_name)
