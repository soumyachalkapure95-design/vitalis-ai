from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('accounts.urls')),
    path('disease-tracker/', include('disease_tracker.urls')),
    path('records/', include('records.urls')),
    path('telemedicine/', include('telemedicine.urls')),
    path('hospitals/', include('hospitals.urls')),
    path('pharmacy/', include('pharmacy.urls')),
    path('mental-health/', include('mental_health.urls')),
    path('emergency/', include('emergency.urls')),
    path('awareness/', include('awareness.urls')),
]
