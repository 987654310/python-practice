data = {'item1': 45, 'item2': 22, 'item3': 78, 'item4': 33}
max_v = data['item1']
max_k = None
min_v = data['item1']
min_k = None

for key,value in data.items():
    if value > max_v:
        max_v = value
        max_k = key
print(f"Maximum value: {max_v}, Key: {max_k}")

for key,value in data.items():
    if value < min_v:
        min_v = value
        min_k = key
print(f"Minimum value: {min_v}, Key: {min_k}")