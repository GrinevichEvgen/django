from django.contrib import admin


# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at",)
    fields = ("title", "content", "author", "created_at",)
    readonly_fields = ("created_at",)
    search_fields = ("title", "author",)
