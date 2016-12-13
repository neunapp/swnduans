from django.contrib import admin

# Register your models here.
from .models import Specialist, Theme

admin.site.register(Specialist)
admin.site.register(Theme)
