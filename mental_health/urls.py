from django.urls import path
from .views import mental_health_home

urlpatterns = [
    path('', mental_health_home, name='mental_health_home'),
]
