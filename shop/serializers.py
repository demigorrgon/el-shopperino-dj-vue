from rest_framework import serializers
from shop.models import Product, Category, CartItem, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(read_only=True)
    category = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
            "price",
            "image",
            "slug",
            "in_stock",
            "category",
            "created_by",
        ]

    def get_created_by(self, obj):
        return obj.created_by.username

    def get_category(self, obj):
        return obj.category.name


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField(read_only=True)

    def get_product(self, obj):
        return obj.product.name

    def to_internal_value(self, data):
        return data

    class Meta:
        model = CartItem
        fields = ("product", "quantity")


class OrderSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    def create(self, validated_data):
        items = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        for item in items:
            cart_item = CartItem.objects.create(
                product=Product.objects.filter(id=item["product"]).first(),
                quantity=item["quantity"],
            )
            order.items.add(cart_item)
        return order

    class Meta:
        model = Order
        fields = (
            "id",
            "items",
            "customer",
            "total_price",
            "created_at",
            "updated_at",
            "confirmed_by_staff",
            "delivered",
        )
