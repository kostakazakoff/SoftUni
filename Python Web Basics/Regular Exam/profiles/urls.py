from django.urls import path, include
from .views import (
    create_profile,
    details_profile,
    edit_profile,
    delete_profile,
)


urlpatterns = [
    path('create/', create_profile, name='create profile'),
    path('details/', details_profile, name='details profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
]