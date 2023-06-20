from django.urls import path, include
from .views import (
    profile_register,
    profile_login,
    profile_edit,
    profile_delete,
    profile_details,
)


urlpatterns = [
    path('register/', profile_register, name='profile register'),
    path('login/', profile_login, name='profile login'),
    path('profile/<int:pk>', include([
        path('', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ]))
]
