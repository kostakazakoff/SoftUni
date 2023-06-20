from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('accounts/', include('accounts.urls')),
    path('pets/', include('pets.urls')),
    path('photos/', include('photos.urls')),
]
