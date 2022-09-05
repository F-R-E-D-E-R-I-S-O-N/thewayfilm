from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('catalog/', films_catalog, name='catalog'),
    path('crew/', crew, name='crew'),
    path('news/', news, name='news')
]
