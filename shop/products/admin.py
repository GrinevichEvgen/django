from django.contrib import admin

from products.models import Product
from purchase.models import Purchase


class PurchaseAdminInline(admin.StackedInline):
    model = Purchase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "price_usd", "color", "description", "created_at")
    fields = ("title", "image", "price", "price_usd", "color", "description", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "description")
    inlines = (PurchaseAdminInline,)

    def save_form(self, request, form, change):
        return super().save_form(request, form, change)

