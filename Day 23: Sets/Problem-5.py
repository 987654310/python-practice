numbers = {1, 2, 3, 4, 5}
num_list = list(numbers)

for a in num_list:
    if a > 3:
        numbers.remove(a)

print(numbers)