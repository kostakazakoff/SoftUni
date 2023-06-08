from django.urls import path
from common.views import home_view, like_functionality

urlpatterns = [
    path('', home_view, name='home'),
    path('photo-like/<int:photo_id>', like_functionality, name='photo like')
]