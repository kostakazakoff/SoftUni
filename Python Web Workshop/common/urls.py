from django.urls import path
from common.views import home_view, like_functionality, copy_link_to_clipboard


urlpatterns = [
    path('', home_view, name='home'),
    path('photo-like/<int:photo_id>', like_functionality, name='photo like'),
    path('photo-share/<int:photo_id>', copy_link_to_clipboard, name='photo share'),
]