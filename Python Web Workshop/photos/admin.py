from django.contrib import admin
from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'date_of_publication', 'get_tagged_pets')

    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join([p.name for p in obj.tagged_pets.all()])
