import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_user_can_create_product(product):
    assert len(product.__class__.objects.all()) == 1


def test_get_all_products(api, product):
    url = reverse("product-list")
    response = api.get(url)
    assert response.data["count"] == 1


def test_get_single_product_by_id(api, product):
    url = reverse("product-detail-pk", kwargs={"pk": product.pk})
    # url = "/api/v1/shop/product/" + product.slug + "/"
    response = api.get(url)
    assert response.status_code == 200
    assert response.data["slug"] is not None


def test_get_single_product_by_slug(api, product):
    url = reverse("product-detail-slug", kwargs={"slug": product.slug})
    # url = "/api/v1/shop/product/" + product.slug + "/"
    response = api.get(url)
    assert response.status_code == 200
    assert response.data["slug"] is not None
