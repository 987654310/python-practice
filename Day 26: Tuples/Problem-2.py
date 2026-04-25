numbers = (1, 2, 3, 2, 4, 2, 5)
numbers_list = list(numbers)

count = 0

for a in numbers_list:
    if a == 2:
        count = count + 1

print(f"2 appears {count} times")