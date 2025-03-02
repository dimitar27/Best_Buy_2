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


def main():


    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()






