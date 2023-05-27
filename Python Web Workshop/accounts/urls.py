from django.urls import path, include
from accounts.views import (
    register_profile,
    login_profile,
    delete_profile,
    details_profile,
    edit_profile,
)

urlpatterns = [
    path('register/', register_profile, name='register profile'),
    path('login/', login_profile, name='login profile'),
    path('profile/<int:pk>/', include([
        path('', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
]