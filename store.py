from products import Product

class Store:
    """Represents a store that manages a collection of products."""

    def __init__(self, products):
        """Initializes a Store object with a list of products"""
        self.products = products

    def add_product(self, product):
        """Adds a product to the store's inventory."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from store's inventory."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        quantity = 0
        for product in self.products:
            quantity += product.get_quantity()
        return quantity

    def get_all_products(self) -> list[Product]:
        """Returns all products in the store that are active."""
        active_products = []

        for product in self.products:
            if product.is_active():
                active_products.append(product)

        return active_products

    def order(self, shopping_list) -> float:
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order."""
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price








