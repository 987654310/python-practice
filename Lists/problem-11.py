quantities = [2, 3, 5, 1]
prices = [50, 30, 20, 10]
total_price = 0

for a in range(0,len(quantities)):
    item_price = prices[a] * quantities[a]
    total_price = total_price + item_price 
print(f"Total price: {total_price}")

