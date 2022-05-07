import pytest
from mixer.backend.django import mixer

from shop.models import Category, Product


@pytest.fixture
def dummy_user(django_user_model):
    return mixer.blend(django_user_model)


@pytest.fixture
def category():
    return mixer.blend(Category)


@pytest.fixture
def product():
    return mixer.blend(Product)
