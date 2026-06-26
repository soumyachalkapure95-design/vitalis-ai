from django.db import models
from django.conf import settings

class EmergencyAlert(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Resolved', 'Resolved'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    description = models.TextField(blank=True, default="Emergency SOS triggered via client dashboard.")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        caller = self.user.username if self.user else "Anonymous Guest"
        return f"SOS Alert from {caller} on {self.created_at}"
