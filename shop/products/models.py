from django.db import models

COLOR_CHOICES = (
    ("RED", "Red"),
    ("GREEN", "Green"),
    ("BLUE", "Blue"),
)
class Product(models.Model):
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=32, choices=COLOR_CHOICES, default="RED")
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

