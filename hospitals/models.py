from django.db import models
from django.conf import settings

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    specialties = models.TextField(help_text="Comma-separated specialties (e.g. Cardiology, Neurology)")
    beds_available = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.0)

    def __str__(self):
        return f"{self.name} ({self.city})"
        
    def get_specialties_list(self):
        return [s.strip() for s in self.specialties.split(',') if s.strip()]

    @property
    def bed_percentage(self):
        # max capacity is 50 based on the template aria-valuemax="50"
        return min(int((self.beds_available / 50) * 100), 100)

class Doctor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctor_profile',
        null=True,
        blank=True
    )
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='doctors')
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    experience = models.IntegerField(default=0)
    consultation_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    available_slots = models.TextField(help_text="Comma-separated slots (e.g. 09:00 AM - 10:00 AM, 02:00 PM - 03:00 PM)")
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.5)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.name

    def get_slots_list(self):
        return [s.strip() for s in self.available_slots.split(',') if s.strip()]
