from abc import ABC, abstractmethod


# ==================== PRODUCT ====================

class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.__price = price
        self.quantity = quantity

    # Getter
    def get_price(self):
        return self.__price

    # Setter
    def set_price(self, price):
        if price <= 0:
            print("Invalid price")
        else:
            self.__price = price
            print("Price updated successfully")

    def calculate_price(self):
        return self.get_price() * self.quantity


# ==================== CUSTOMER ====================

class Customer:
    def __init__(self, customer_name, email, address):
        self.customer_name = customer_name
        self.email = email
        self.address = address


# ==================== SHOPPING CART ====================

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)

    def show_cart(self):
        for product in self.items:
            print(f"Product: {product.product_name}")
            print(f"Price: ₹{product.get_price()}")
            print(f"Quantity: {product.quantity}")
            print(f"Calculated Price: ₹{product.calculate_price()}")
            print("-" * 30)

    def calculate_total(self):
        total = 0

        for product in self.items:
            total += product.calculate_price()

        return total


# ==================== ELECTRONIC PRODUCT ====================

class ElectronicProduct(Product):
    def __init__(self, product_name, price, quantity, warranty):
        super().__init__(product_name, price, quantity)
        self.warranty = warranty

    def calculate_price(self):
        price = self.get_price() * self.quantity
        gst = price * 18 / 100
        return price + gst


# ==================== CLOTHING PRODUCT ====================

class ClothingProduct(Product):
    def __init__(self, product_name, price, quantity, size):
        super().__init__(product_name, price, quantity)
        self.size = size

    def calculate_price(self):
        price = self.get_price() * self.quantity
        discount = price * 10 / 100
        return price - discount


# ==================== PAYMENT ====================

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Payment of ₹{amount:.2f} successful through UPI")


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Payment of ₹{amount:.2f} successful through Card")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Payment of ₹{amount:.2f} successful through Cash")


# ==================== ORDER ====================

class Order:
    def __init__(self, order_id, customer, cart):
        self.order_id = order_id
        self.customer = customer
        self.cart = cart

    def show_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer.customer_name}")
        print(f"Cart Total: ₹{self.get_total():.2f}")
        print(f"Final Amount: ₹{self.calculate_final_amount():.2f}")

    def get_total(self):
        return self.cart.calculate_total()

    def calculate_final_amount(self):
        total = self.get_total()

        # Apply 10% discount on the order
        discount = total * 10 / 100

        return total - discount

    def make_payment(self, payment):
        final_amount = self.calculate_final_amount()
        payment.pay(final_amount)


# ==================== MAIN PROGRAM ====================

customer = Customer(
    "Shruti",
    "shruti@gmail.com",
    "Delhi"
)


# Create products
keyboard = Product("Keyboard", 1500, 2)

mouse = Product("Mouse", 800, 2)

laptop = ElectronicProduct(
    "Laptop",
    60000,
    1,
    "2 Years"
)

tshirt = ClothingProduct(
    "T-Shirt",
    1500,
    2,
    "M"
)


# Create shopping cart
cart = ShoppingCart()

cart.add_product(keyboard)
cart.add_product(mouse)
cart.add_product(laptop)
cart.add_product(tshirt)


# Display cart
print("=" * 40)
print("          SHOPPING CART")
print("=" * 40)

cart.show_cart()

print(f"Cart Total: ₹{cart.calculate_total():.2f}")


# Create order
order = Order(101, customer, cart)

print("\n" + "=" * 40)
print("             ORDER")
print("=" * 40)

order.show_order()


# Payment
print("\n" + "=" * 40)
print("            PAYMENT")
print("=" * 40)

upi = UPIPayment()
order.make_payment(upi)

card = CardPayment()
order.make_payment(card)

cash = CashPayment()
order.make_payment(cash)
