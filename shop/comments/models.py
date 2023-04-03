from django.conf import settings
from django.db import models


class Comment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                               related_name="comment")

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)


    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.title = None

    def __str__(self):
        return self.title




