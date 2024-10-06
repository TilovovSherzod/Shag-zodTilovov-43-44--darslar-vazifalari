from django.urls import path
from .views import first, second, pages

urlpatterns = [
    path('', first, name='first_page'),
    path('second/', second, name='second_page'),
    path('pages/<str:page>', pages, name='second_page'),
]