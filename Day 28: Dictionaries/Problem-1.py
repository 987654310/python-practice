sum = 0

shopping_cart = {
    "apple": 2.5,
    "banana": 1.2,
    "milk": 3.0,
    "bread": 2.0
}

for items, price in shopping_cart.items():
    sum = sum + price

print(f"The total price of all of the items is {sum}")