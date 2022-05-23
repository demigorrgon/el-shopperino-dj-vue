import pytest
from profiles.models import Profile

pytestmark = pytest.mark.django_db


def test_user_profile_created_on_user_creation(api_user_to_login):
    assert Profile.objects.count() == 1
