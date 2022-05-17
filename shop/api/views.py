from rest_framework import viewsets
from shop.models import Product, Order
from shop.serializers import ProductSerializer, OrderSerializer
from django.shortcuts import get_object_or_404

# from rest_framework import pagination


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # pagination_class = pagination.PageNumberPagination
    page_size = 10

    def get_object(self, queryset=None, **kwargs):
        if self.kwargs.get("pk"):
            obj = self.kwargs.get("pk")
            return get_object_or_404(Product, id=obj)

        return get_object_or_404(Product, slug=self.kwargs.get("slug"))


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_object(self, queryset=None, **kwargs):
        if self.kwargs.get("pk"):
            obj = self.kwargs.get("pk")
            return get_object_or_404(Order, id=obj)
