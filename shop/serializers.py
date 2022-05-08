from rest_framework import serializers
from shop.models import Product, Category


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
