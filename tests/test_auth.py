"""Test auth module"""
from os import environ
from os import getenv
from random import randint

import pytest
from dotenv import load_dotenv

from pilk_clicker.api import Auth
from pilk_clicker.interfaces.auth import ILoginRequest
from pilk_clicker.interfaces.auth import ILogupRequest
from pilk_clicker.interfaces.auth import ITokenRequest


load_dotenv()


def test_login():
    """Test login method"""
    credentials = ILoginRequest(
        username=getenv("USERNAME"), password=getenv("PASSWORD")
    )
    response = Auth.login(credentials)
    environ["TOKEN"] = response.auth_token
    assert response.auth_token is not None


def test_logout():
    """Test logout method"""
    credentials = ITokenRequest(authorization=environ["TOKEN"])
    Auth.logout(credentials)
    assert True


def test_logup():
    """Test logup method"""
    credentials = ILogupRequest(
        username="test_" + str(randint(0, 100000)),
        password="test" + str(randint(0, 100000)) + "rt$$$",
        email="test" + str(randint(0, 100000)) + "@test.com",
    )
    response = Auth.logup(credentials)
    assert response.username == credentials.username
