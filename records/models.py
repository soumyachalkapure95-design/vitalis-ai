from django.db import models
from accounts.models import CustomUser

class HealthRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=5)
    allergies = models.TextField(blank=True)
    medications = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username