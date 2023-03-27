from django.contrib import admin

from purchase.models import Purchase
from products.models import Product


class PurchaseAdminInline(admin.StackedInline):
    model = Purchase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "price", "description", "color", "created_at")
    fields = ("title", "image", "price", "description", "color", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "description")
    inlines = (PurchaseAdminInline,)
