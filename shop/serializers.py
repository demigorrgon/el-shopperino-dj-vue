from rest_framework import serializers
from shop.models import Product, Category, CartItem, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
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

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d-%m-%Y %H:%M %Z")

    def get_category(self, obj):
        return obj.category.name

    # def create(self, validated_data):
    #     print(validated_data)


class ProductCreateSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ("category", "name", "description", "price", "image")


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)
    price = serializers.SerializerMethodField(read_only=True)

    def get_product(self, obj):
        return obj.product.name

    def get_price(self, obj):
        return obj.product.price

    def get_image(self, obj):
        return f"http://127.0.0.1:8000{obj.product.image.url}"

    def to_internal_value(self, data):
        return data

    class Meta:
        model = CartItem
        fields = ("product", "quantity", "image", "price")


class OrderSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField(read_only=True)
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

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d-%m-%Y %H:%M %Z")

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
