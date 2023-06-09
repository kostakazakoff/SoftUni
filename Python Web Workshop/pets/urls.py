from django.urls import path, include
from pets.views import (
    add_pet,
    delete_pet,
    details_pet,
    edit_pet,
)

urlpatterns = [
    path('add/', add_pet, name='add_pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', details_pet, name='details pet'),
        path('edit/', edit_pet, name='edit pet'),
        path('delete/', delete_pet, name='delete pet')
    ]))
]
