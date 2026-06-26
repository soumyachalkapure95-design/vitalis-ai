from django.urls import path
from .views import disease_predict

urlpatterns = [
    path('', disease_predict, name='predict'),
]