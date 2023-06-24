from django.contrib import admin
from .models import Fruit


@admin.register(Fruit)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'nutrition', 'id')
