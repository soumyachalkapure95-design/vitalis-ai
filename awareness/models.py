from django.db import models

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('Fitness', 'Fitness'),
        ('Nutrition', 'Nutrition'),
        ('Hygiene', 'Hygiene'),
        ('Preventive Care', 'Preventive Care'),
    ]

    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=300, help_text="Brief summary of the article")
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    read_time = models.IntegerField(default=5, help_text="Estimated read time in minutes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.category})"
