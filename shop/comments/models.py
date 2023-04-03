from django.db import models


# Create your models here.


class Comment(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
