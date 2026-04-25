members = [
    {"name": "Amit", "age": 25, "membership": "Gold", "visits": 22},
    {"name": "Neha", "age": 30, "membership": "Silver", "visits": 12},
    {"name": "Ravi", "age": 21, "membership": "Bronze", "visits": 5},
    {"name": "Pooja", "age": 35, "membership": "Gold", "visits": 28},
    {"name": "Rakesh", "age": 45, "membership": "Silver", "visits": 19},
    {"name": "Sneha", "age": 29, "membership": "Gold", "visits": 30},
    {"name": "Raj", "age": 38, "membership": "Bronze", "visits": 8},
    {"name": "Tina", "age": 26, "membership": "Gold", "visits": 25},
    {"name": "Manoj", "age": 33, "membership": "Silver", "visits": 15},
    {"name": "Nikita", "age": 24, "membership": "Bronze", "visits": 2}
]

for a in members:
    if a["membership"] == "Gold" and a["visits"] > 20:
        print(a)
print("------------------------------------------")
for i in members:    
    if i["age"] < 30 and i["visits"] < 10:
        print(i)