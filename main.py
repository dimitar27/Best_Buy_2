from products import Product, NonStockedProduct, LimitedProduct
from store import Store
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount

def start(store_object):
    """Handles the store menu and user interactions."""
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            user_input = int(input("Please choose a number: "))
            if user_input < 1 or user_input > 4:
                raise ValueError
        except ValueError:
            print("Error with your choice! Try again!")
            continue

        if user_input == 1:
            print("------")
            for index, product in enumerate(store_object.get_all_products(), start=1):
                print(f"{index}. {product.show()}")
            print("------")

        elif user_input == 2:
            print(f"Total of {store_object.get_total_quantity()} in store")

        elif user_input == 3:
            shopping_list = []
            product_mapping = {}

            print("------")
            for index, product in enumerate(store_object.get_all_products(), start=1):
                print(f"{index}. {product.show()}")
                product_mapping[index] = product
            print("------")

            print("\nWhen you want to finish order, enter empty text.")

            while True:

                user_product_choice = input("Which product # do you want? ")
                if user_product_choice == "":
                    break

                try:
                    user_product_choice = int(user_product_choice)
                    product_amount = int(input("What amount do you want? "))

                    selected_product = product_mapping.get(user_product_choice)

                    if selected_product is None:
                        print("Error adding product!")
                        continue

                    shopping_list.append((selected_product, product_amount))
                    print("Product added to list!\n")

                except ValueError:
                    print("Error adding product!")
            try:
                total_payment = store_object.order(shopping_list)
                print(f"********")
                print(f"Order made! Total payment: ${total_payment:.2f}")
            except ValueError:
                print("Error while making order! Quantity larger than what exists")


        elif user_input == 4:
            break


def main():
    # setup initial stock of inventory
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = Store(product_list)

    start(best_buy)

if __name__ == "__main__":
    main()
