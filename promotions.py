from abc import ABC, abstractmethod

class Promotion(ABC):
    """Abstract class for all promotions."""

    def __init__(self, name):
        """Initializes a promotion with a name."""
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """Applies the promotion and returns the total discounted price."""
        pass


class PercentDiscount(Promotion):
    """Applies a percentage discount to a product."""

    def __init__(self, name, percent):
        """Initializes a percentage discount promotion."""
        super().__init__(name)
        self.discount_percent = percent

    def apply_promotion(self, product, quantity) -> float:
        """Applies the percentage discount to the total price."""
        discount = product.price * (self.discount_percent / 100)
        return (product.price - discount) * quantity


class SecondHalfPrice(Promotion):
    """Applies a discount where every second item is half price."""

    def __init__(self, name):
        """Initializes the second half price promotion."""
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        """Calculates the total price where every second item is half price."""
        full_price_items = (quantity // 2) + (quantity % 2)
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * (product.price * 0.5))


class ThirdOneFree(Promotion):
    """Every third item is free."""

    def __init__(self, name):
        """Initializes the buy 2, get 1 free promotion."""
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        """Calculates the total price where every third item is free."""
        payable_quantity = quantity - (quantity // 3)
        return payable_quantity * product.price
