from django.db import models
from django.conf import settings

# Create your models here.


class Comment(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                               related_name="notes")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
