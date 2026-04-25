numbers = set(range(1, 11))

for a in range(1,len(numbers) + 1):
    if a % 3 == 0:
        numbers.remove(a)
print(numbers)

numbers.add(11)

numbers.add(12)

print(sorted(numbers))
