from django.contrib import admin
from .models import PhotoComment

@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    list_display = ('publication_date_time', 'to_photo')