from django.contrib import admin
from .models import Photo

@admin.register(Photo)
class PetAdmin(admin.ModelAdmin):
    list_display = ('description', 'get_tagged_pets', 'id')
