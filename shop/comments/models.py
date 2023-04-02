from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


# Create your models here.
