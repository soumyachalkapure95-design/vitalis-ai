from django.urls import path
from .views import records_list, add_record, edit_record, delete_record

urlpatterns = [
    path('', records_list, name='records_list'),
    path('add/', add_record, name='add_record'),
    path('edit/<int:pk>/', edit_record, name='edit_record'),
    path('delete/<int:pk>/', delete_record, name='delete_record'),
]
