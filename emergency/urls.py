from django.urls import path
from .views import emergency_home, trigger_sos

urlpatterns = [
    path('', emergency_home, name='emergency_home'),
    path('sos/', trigger_sos, name='trigger_sos'),
]
