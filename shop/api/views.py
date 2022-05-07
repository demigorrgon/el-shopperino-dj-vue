from rest_framework import viewsets
from shop.models import Product
from shop.serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework import pagination


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = pagination.PageNumberPagination
    page_size = 10

    def get_object(self, queryset=None, **kwargs):
        obj = self.kwargs.get("pk")
        return get_object_or_404(Product, slug=obj)
