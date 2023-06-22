from django.urls import path
from .views import home, like_functionality, share_functionality


urlpatterns = [
    path('', home, name='home'),
    path('like/<int:id>/', like_functionality, name='photo like'),
    path('share/<int:id>/', share_functionality, name='photo share')
]