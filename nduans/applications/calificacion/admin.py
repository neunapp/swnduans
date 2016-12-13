from django.contrib import admin

# Register your models here.
from .models import ThemeRating, SpecialistRating

admin.site.register(ThemeRating)
admin.site.register(SpecialistRating)
