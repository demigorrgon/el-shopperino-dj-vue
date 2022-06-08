from rest_framework import viewsets, status
from rest_framework.response import Response
from authapp.models import CustomUser
from shop.models import Product, Order, Category
from shop.serializers import (
    ProductSerializer,
    OrderSerializer,
    CategorySerializer,
    ProductCreateSerializer,
)
from django.shortcuts import get_object_or_404
from django.utils.text import slugify


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    # serializer_class = ProductSerializer
    # pagination_class = pagination.PageNumberPagination
    page_size = 10

    def get_object(self, queryset=None, **kwargs):
        if self.kwargs.get("pk"):
            obj = self.kwargs.get("pk")
            return get_object_or_404(Product, id=obj)

        return get_object_or_404(Product, slug=self.kwargs.get("slug"))

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductSerializer

        return ProductCreateSerializer

    # add permission checking is_staff. only staff should create products
    def create(self, request):
        data = request.data
        category = Category.objects.get(id=data["category"])
        user = CustomUser.objects.get(username=data["user"])
        name_to_slug = slugify(data["name"])
        product = Product.objects.create(
            category=category,
            name=data["name"],
            description=data["description"],
            price=data["price"],
            image=data["image"],
            created_by=user,
            slug=name_to_slug,
        )
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_object(self, queryset=None, **kwargs):
        if self.kwargs.get("pk"):
            obj = self.kwargs.get("pk")
            return get_object_or_404(Order, id=obj)


class UsersOrdersViewSet(viewsets.ModelViewSet):
    # queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.kwargs["pk"]:
            id = self.kwargs["pk"]
            return Order.objects.filter(customer=id)

    def get_object(self, *args, **kwargs):
        if self.kwargs["order_id"]:
            order_id = self.kwargs["order_id"]
            return Order.objects.filter(id=order_id).first()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
