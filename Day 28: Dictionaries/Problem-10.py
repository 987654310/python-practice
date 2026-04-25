dict1 = {'x': 1, 'y': 2, 'z': 3}
dict2 = {'w': 10, 'x': 11, 'y': 22}
l = []

for key in dict1:
    if key in dict2:
        l.append(key)
print(l)

