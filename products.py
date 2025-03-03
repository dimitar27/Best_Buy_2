class Product:
    """Represents a product with a name, price, quantity, and active status."""

    def __init__(self, name, price, quantity):
        """Initializes a Product instance."""

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name is required and cannot be blank.")

        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")

        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Error: Quantity must be at least 1.")

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self) -> int:
        """Getter function for quantity.
        Returns the quantity (int)."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

    def get_promotion(self):
        """Returns the current promotion applied to the product."""
        return self.promotion

    def set_promotion(self, promotion):
        """Assigns a promotion to the product."""
        self.promotion = promotion

    def is_active(self) -> bool:
        """Getter function for active.
        Returns True if the product is active, otherwise False."""
        return self.quantity > 0

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self) -> str:
        """Returns a string that represents the product"""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem, raises an Exception"""

        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(quantity)
        return total_price


class NonStockedProduct(Product):
    """Represents a product that does not track quantity."""

    def __init__(self, name, price):
        """Initializes a non-stocked product with a fixed price and no quantity tracking."""
        super().__init__(name, price, quantity=1)
        self.quantity = 0

    def show(self):
        """Returns the product with unlimited quantity."""
        if self.promotion:
            promo_text = f" - Promotion: {self.promotion.name}"
        else:
            promo_text = ""

        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo_text}"

    def is_active(self) -> bool:
        """Always returns True, since non-stocked products are always available."""
        return True

    def buy(self, quantity):
        """Calculates the total price for the given quantity."""
        return self.price * quantity


class LimitedProduct(Product):
    """Represents a product that has a purchase limit per order."""

    def __init__(self, name, price, quantity, maximum):
        """Initializes a limited product with a maximum purchase restriction."""
        super().__init__(name, price, quantity)
        if not isinstance(maximum, int) or maximum <= 0:
            raise ValueError("Maximum purchase limit must be a positive integer.")
        self.maximum = maximum

    def show(self) -> str:
        """Returns a string containing the product details."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity} (Max {self.maximum} per order)"

    def buy(self, quantity) -> float:
        """Ensures that the purchase does not exceed the maximum limit."""
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} per order.")
        return super().buy(quantity)









