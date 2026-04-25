num = [10,5,8,12,3]
print(num)
max = num[0]
min = num[0]
for a in num:
    if a > max:
        max = a
    if a < min:
        min = a
print(f"Maximum value: {max}")
print(f"Minimum value: {min}")