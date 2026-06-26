from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    use = models.TextField()
    dosage = models.TextField(default="As directed by physician")
    side_effects = models.TextField(default="None reported")
    category = models.CharField(max_length=100, default="General")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    image = models.URLField(max_length=500, blank=True, default="")

    def __str__(self):
        return self.name