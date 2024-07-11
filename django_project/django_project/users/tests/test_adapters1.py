import pytest
from django.http import HttpRequest
from django.conf import settings
from django_project.users.adapters import AccountAdapter

@pytest.fixture
def your_instance():
    return AccountAdapter()

def test_is_open_for_signup_when_registration_allowed(your_instance):
    settings.ACCOUNT_ALLOW_REGISTRATION = True
    request = HttpRequest()
    result = your_instance.is_open_for_signup(request)
    assert result is True

def test_is_open_for_signup_when_registration_not_allowed(your_instance):
    settings.ACCOUNT_ALLOW_REGISTRATION = False
    request = HttpRequest()
    result = your_instance.is_open_for_signup(request)
    assert result is False
