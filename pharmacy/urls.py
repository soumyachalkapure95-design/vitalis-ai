from django.urls import path
from .views import medicine_list

urlpatterns = [
    path('', medicine_list, name='medicine_list'),
]
