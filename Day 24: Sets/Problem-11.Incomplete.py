numbers = set(range(1, 21)) 
numbers_list = list(numbers)

for a in numbers_list:
    if a > 2: 
        prime = True
        for b in range(2,a):
            if a % b == 0:
                prime = False
                break

        print(prime)

if prime == True:
    numbers.remove(a)

print(numbers)
