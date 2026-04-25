numbers = {
    "a": 10,
    "b": 15,
    "c": 5,
    "d": 20
}
threshold = 12
x = []

for y,z in numbers.items():
    if threshold < z:
        x.append(y)
for key in x :
    numbers.pop(key)
print(numbers)