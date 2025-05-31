# create a class called order which stores item & its price.
# use Dander function __gt__() to convey that:order1>order2 if price of order1>price of order2.
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price

    def __str__(self):
        return f"Item: {self.item}, Price: {self.price}"


# Example usage
order1 = Order("Laptop", 1500)
order2 = Order("Smartphone", 800)
print(order1)  # Output: Item: Laptop, Price: 1500
print(order2)  # Output: Item: Smartphone, Price: 800
print(order1 > order2)  # Output: True, since 1500 > 800
print(order2 > order1)  # Output: False, since 800 < 1500
