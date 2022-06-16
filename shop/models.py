from django.db import models

from authapp.models import CustomUser

# from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(max_length=255)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="images/")
    slug = models.SlugField(max_length=100, unique=True)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    items = models.ManyToManyField(CartItem)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    country_deliver_to = models.CharField(max_length=50)
    region_deliver_to = models.CharField(max_length=100)
    postal_address = models.CharField(max_length=250)
    delivery_coordinates = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    confirmed_by_staff = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
