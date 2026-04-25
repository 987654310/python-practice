n = input("n: ")
n = int(n)

sum = 0
for number in range(1, n +1):
    if number % 6 == 0:
        sum = sum + number
print(f"Sum: {sum}")
    

