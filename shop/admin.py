from django.contrib import admin
from shop.models import Category, Product, CartItem, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "created_by",
        "slug",
        "price",
        "in_stock",
        "created_at",
        "updated_at",
    ]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ["in_stock", "is_active"]
    list_editable = ["price", "in_stock"]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "quantity",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "show_items",
        "customer",
        "total_price",
        "created_at",
    )

    def show_items(self, obj):
        return "\n".join([item.product.name for item in obj.items.all()])
