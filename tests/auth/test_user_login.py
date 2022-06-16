from django.urls import reverse
import pytest

pytestmark = pytest.mark.django_db


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
