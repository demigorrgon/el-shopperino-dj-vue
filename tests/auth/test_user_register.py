from django.urls import reverse
import pytest

pytestmark = pytest.mark.django_db


def test_user_can_register(api):
    url = reverse("user-list")
    response = api.post(
        url,
        {
            "username": "kekker",
            "password": "somepassword1",
            "email": "some@mail.com",
            "first_name": "I",
            "last_name": "wasda",
        },
    )
    assert response.status_code == 201
