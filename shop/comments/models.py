from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.title = None

    def __str__(self):
        return self.title


# Create your models here.
