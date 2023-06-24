from django.urls import path, include
from .views import (
    index,
    dashboard,
    create_fruit,
    fruit_details,
    edit_fruit,
    delete_fruit,
)


urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', create_fruit, name='create fruit'),
    path('<int:id>/', include([
        path('details/', fruit_details, name='fruit details'),
        path('edit/', edit_fruit, name='edit fruit'),
        path('delete/', delete_fruit, name='delete fruit')
    ]))
]
