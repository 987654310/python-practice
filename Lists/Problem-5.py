list = [1, 3, 7, 8, 3, 5, 3]
print(f"List: {list}")
target_number = input("Target Number ")
target_number = int(target_number)

count = 0
for a in list:
    if a == target_number:
        count = count + 1
print(f"{target_number} appears {count} times")