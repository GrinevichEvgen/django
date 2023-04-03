from django.contrib import admin
from .models import Comment


# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    author = ("title", "author", "created_at",)
    fields = ("title", "content", "author", "created_at",)
    readonly_fields = ("created_at",)
    search_fields = ("title", "author",)



