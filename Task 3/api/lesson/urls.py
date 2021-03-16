from django.urls import path

from .views import *


urlpatterns = [
    path('total_appearance/', index, name='total_appearance'),
]