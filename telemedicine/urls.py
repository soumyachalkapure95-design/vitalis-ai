from django.urls import path
from .views import appointment_list, book_appointment, manage_appointment

urlpatterns = [
    path('', appointment_list, name='appointment_list'),
    path('book/', book_appointment, name='book_appointment'),
    path('manage/<int:pk>/', manage_appointment, name='manage_appointment'),
]
