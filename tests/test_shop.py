"""Test shop module"""
from os import getenv

import pytest
from dotenv import load_dotenv

from pilk_clicker.api import Auth
from pilk_clicker.api import Shop
from pilk_clicker.interfaces.auth import ILoginRequest
from pilk_clicker.interfaces.auth import ITokenRequest
from pilk_clicker.interfaces.shop import ISaveItemRequest


load_dotenv()


class TestShop:
    """Test shop module"""

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

    def test_shop_user(self):
        """Test shop_user method"""
        response = Shop.shop_user(ITokenRequest(authorization=self.token))
        assert response is not None

    def test_save_item(self):
        """Test save_item method"""
        items = Shop.shop_user(ITokenRequest(authorization=self.token))
        response = Shop.save_item(
            data=ISaveItemRequest(id=items[0].id, amount=items[0].amount + 1),
            credentials=ITokenRequest(authorization=self.token),
        )
        assert response is not None
