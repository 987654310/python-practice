numbers = (0, 1, 45, 34, 7, 98, 12)

maximum = 0
minimum = 0

for a in numbers:
    if a > maximum:
        maximum = a
    if a <= minimum:
        minimum = a

print(maximum)
print(minimum)
