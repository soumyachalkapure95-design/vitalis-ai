from django.db import models
from django.conf import settings
from django.utils import timezone

class MoodLog(models.Model):
    MOOD_CHOICES = [
        ('Happy', 'Happy (😊)'),
        ('Calm', 'Calm (😌)'),
        ('Anxious', 'Anxious (😰)'),
        ('Sad', 'Sad (😢)'),
        ('Tired', 'Tired (😴)'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date = models.DateField(default=timezone.now)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.mood} on {self.date}"
