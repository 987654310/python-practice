numbers = (10, 15, 20, 25, 30, 35, 40)
numbers_list = list()

for a in numbers:
    if a % 20 == 0:
        numbers_list.append(a)

numbers_tuple = tuple(numbers_list)
print(numbers_tuple)
