"""Test clicker module"""
from os import environ
from os import getenv
from random import randint

import pytest
from dotenv import load_dotenv

from pilk_clicker.api import Auth
from pilk_clicker.api import Clicker
from pilk_clicker.interfaces.auth import ILoginRequest
from pilk_clicker.interfaces.auth import ITokenRequest
from pilk_clicker.interfaces.clicker import IClickerSaveRequest


load_dotenv()


class TestClicker:
    """Test clicker module"""

    @classmethod
    def setup_class(cls):
        """Setup class"""
        cls.credentials = ILoginRequest(
            username=getenv("USERNAME"), password=getenv("PASSWORD")
        )
        cls.login_response = Auth.login(cls.credentials)
        cls.token = cls.login_response.auth_token

    @classmethod
    def teardown_class(cls):
        """Teardown class"""
        Auth.logout(ITokenRequest(authorization=cls.token))

    def test_clicker_detail(self):
        """Test clicker_detail method"""
        response = Clicker.clicker_detail(ITokenRequest(authorization=self.token))
        assert response.arcoin_amount is not None

    def test_top_list(self):
        """Test top_list method"""
        response = Clicker.top_list(ITokenRequest(authorization=self.token))
        assert response is not None

    def test_save_clicker(self):
        """Test save_clicker method"""
        response = Clicker.save_clicker(
            data=IClickerSaveRequest(
                arcoin_amount=randint(0, 100000),
                arcoins_per_click=randint(0, 100000),
                arcoins_per_seconds=randint(0, 100000),
            ),
            credentials=ITokenRequest(authorization=self.token),
        )
        assert response.arcoin_amount is not None
