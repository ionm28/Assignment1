import pytest
from django.http import HttpRequest
from django.conf import settings
from django_project.users.adapters import AccountAdapter

@pytest.fixture
def my_instance():
    return AccountAdapter()

#second function
def test_is_open_for_signup_registration_allowed(my_instance):
    settings.ACCOUNT_ALLOW_REGISTRATION = True
    request = HttpRequest()
    result = my_instance.is_open_for_signup(request)
    assert result is True

def test_is_open_for_signup_registration_not_allowed(my_instance):
    settings.ACCOUNT_ALLOW_REGISTRATION = False
    request = HttpRequest()
    result = my_instance.is_open_for_signup(request)
    assert result is False