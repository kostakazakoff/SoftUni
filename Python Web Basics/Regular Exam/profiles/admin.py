from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class PetAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'age', 'id')
