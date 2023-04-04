from django.contrib import admin

from comments.models import Comment


# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at",)
    fields = ("title", "content", "created_at",)
    readonly_fields = ("created_at",)
    search_fields = ("title",)
