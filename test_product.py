import pytest
from products import Product


def test_create_product():
    """Tests creating a valid product"""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450.0
    assert product.quantity == 100
    assert product.is_active() is True


def test_create_product_invalid_details():
    """Test if creating a product with invalid details (empty name, negative price, zero quantity)
       raises the expected exceptions."""

    with pytest.raises(ValueError, match="Product name is required and cannot be blank."):
        Product("", price=1450, quantity=100)

    with pytest.raises(ValueError, match="Price must be a positive number."):
        Product("MacBook Air M2", price=-10, quantity=100)

    with pytest.raises(ValueError, match="Error: Quantity must be at least 1."):
        Product("MacBook Air M2", price=1450, quantity=0)


def test_product_becomes_inactive():
    """Test that a product becomes inactive when its quantity reaches zero."""
    product = Product("Google Pixel 7", price=500, quantity=1)
    product.buy(1)
    assert product.is_active() is False


def test_product_buy():
    """Test that purchasing a product modifies the quantity and returns the correct total price."""
    product = Product("Bose QuietComfort Earbuds", price=250, quantity=10)
    total_price = product.buy(2)
    assert total_price == 500
    assert product.quantity == 8


def test_buy_more_than_available():
    """Test that buying a larger quantity than available raises an exception."""
    product = Product("MacBook Air M2", price=1450, quantity=5)
    with pytest.raises(ValueError, match="Not enough stock available."):
        product.buy(10)
