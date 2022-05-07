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


def test_user_retrieve_token_on_login(api, api_user_to_login):
    url = reverse("token_obtain_pair")
    response = api.post(
        url,
        {
            "username": api_user_to_login.username,
            "password": "12345",
        },
    )
    print(api_user_to_login.username, api_user_to_login.password)
    assert response.status_code == 200


def test_token_returned_on_login(api, api_user_to_login):
    url = reverse("token_obtain_pair")
    response = api.post(
        url,
        {
            "username": api_user_to_login.username,
            "password": "12345",
        },
    )
    assert response.data["access"]
