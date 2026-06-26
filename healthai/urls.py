from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('accounts.urls')),
    path('records/', include('records.urls')),
    path('pharmacy/', include('pharmacy.urls')),
    path('disease/', include('disease_tracker.urls')),
    path('mental/', include('mental_health.urls')),
]