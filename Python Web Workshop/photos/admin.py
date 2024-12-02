from django.contrib import admin
from .models import Photo

@admin.register(Photo)
class PetAdmin(admin.ModelAdmin):
    list_display = ('description', 'date_of_publication', 'get_tagged_pets', 'id')
