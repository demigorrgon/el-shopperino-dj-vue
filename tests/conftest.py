import pytest
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from shop.models import Category, Product


@pytest.fixture
def dummy_user(django_user_model):
    return mixer.blend(django_user_model)


@pytest.fixture
def api_user_to_login():
    return User.objects.create_user(
        username="kekker1",
        password="12345",
        email="some@mail.com",
        first_name="I",
        last_name="wasda",
    )


@pytest.fixture
def category():
    return mixer.blend(Category)


@pytest.fixture
def product():
    return mixer.blend(Product)


@pytest.fixture
def api():
    client = APIClient()
    return client


test_commit
