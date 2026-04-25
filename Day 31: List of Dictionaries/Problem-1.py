products = [
    {"name": "Laptop", "price": 55000, "category": "Electronics", "rating": 4.5},
    {"name": "T-shirt", "price": 500, "category": "Clothing", "rating": 4.0},
    {"name": "Smartphone", "price": 30000, "category": "Electronics", "rating": 4.7},
    {"name": "Jeans", "price": 1200, "category": "Clothing", "rating": 4.2},
    {"name": "Air Fryer", "price": 8000, "category": "Home Appliances", "rating": 4.3},
    {"name": "Headphones", "price": 2000, "category": "Electronics", "rating": 3.9},
    {"name": "Shoes", "price": 2500, "category": "Footwear", "rating": 4.1},
    {"name": "Refrigerator", "price": 45000, "category": "Home Appliances", "rating": 4.6},
    {"name": "Dress", "price": 1800, "category": "Clothing", "rating": 4.4},
    {"name": "Microwave", "price": 9500, "category": "Home Appliances", "rating": 4.0}
]

for a in products:
    if a['category'] == 'Electronics' and a['price'] < 10000 and a['rating'] >= 4.5:
        print(a)

for b in products:
    if b["category"] == 'Clothing' and b['rating'] > 4.0:
        print(b)


