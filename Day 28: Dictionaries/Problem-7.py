a = []
inventory = {
    "pen": 10,
    "pencil": 0,
    "eraser": 5,
    "notebook": 0
}

for y,z in inventory.items():
    if z == 0:
        a.append(y)
for key in a :
    inventory.pop(key)
print(inventory)