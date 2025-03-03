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

    def get_quantity(self) -> int:
        """Getter function for quantity.
        Returns the quantity (int)."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative whole number")

        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

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
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Please enter a whole number greater than zero.")

        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False

        return total_price


class NonStockedProduct(Product):
    """Represents a product that does not track quantity."""

    def __init__(self, name, price):
        """Initializes a non-stocked product with a fixed price and no quantity tracking."""
        super().__init__(name, price, quantity=1)
        self.quantity = 0

    def show(self):
        """Returns the product with unlimited quantity."""
        return f"{self.name}, Price: {self.price} (unlimited quantity)"

    def is_active(self):
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

    def buy(self, quantity) -> float:
        """Ensures that the purchase does not exceed the maximum limit."""
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} per order.")
        return super().buy(quantity)

    def show(self) -> str:
        """Returns a string containing the product details."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity} (Max {self.maximum} per order)"







