from django.db import models
from django.conf import settings

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    SLOT_CHOICES = [
        ('09:00 AM - 10:00 AM', '09:00 AM - 10:00 AM'),
        ('10:00 AM - 11:00 AM', '10:00 AM - 11:00 AM'),
        ('11:00 AM - 12:00 PM', '11:00 AM - 12:00 PM'),
        ('02:00 PM - 03:00 PM', '02:00 PM - 03:00 PM'),
        ('03:00 PM - 04:00 PM', '03:00 PM - 04:00 PM'),
        ('04:00 PM - 05:00 PM', '04:00 PM - 05:00 PM'),
    ]

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='patient_appointments'
    )
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctor_appointments'
    )
    date = models.DateField()
    time_slot = models.CharField(max_length=50, choices=SLOT_CHOICES)
    symptoms = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appt #{self.id}: {self.patient.username} with {self.doctor.username}"
