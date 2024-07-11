import pytest
from django.http import HttpRequest
from django.conf import settings
from django_project.users.adapters import SocialAccountAdapter

@pytest.fixture
def my_instance():
    return SocialAccountAdapter()

#second function
def test_is_open_for_signup_registration_allowed_no_sociallogin(my_instance):
    settings.ACCOUNT_ALLOW_REGISTRATION = True
    request = HttpRequest()
    sociallogin = None
    result = my_instance.is_open_for_signup(request, sociallogin)
    assert result is True

def test_is_open_for_signup_registration_allowed_with_sociallogin(my_instance):
    settings.ACCOUNT_ALLOW_REGISTRATION = True
    request = HttpRequest()
    sociallogin = SocialAccountAdapter() 
    result = my_instance.is_open_for_signup(request, sociallogin)
    assert result is True

def test_is_open_for_signup_registration_not_allowed_no_sociallogin(my_instance):
    settings.ACCOUNT_ALLOW_REGISTRATION = False
    request = HttpRequest()
    sociallogin = None  
    result = my_instance.is_open_for_signup(request, sociallogin)
    assert result is False

def test_is_open_for_signup_registration_not_allowed_with_sociallogin(my_instance):
    settings.ACCOUNT_ALLOW_REGISTRATION = False
    request = HttpRequest()
    sociallogin = SocialAccountAdapter()  
    result = my_instance.is_open_for_signup(request, sociallogin)
    assert result is False