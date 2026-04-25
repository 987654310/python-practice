number = input("Number: ")
number = int(number)
result = 1
m = 1

for m in range(1,10 + 1, 1):
    result = m * number
    if result % 2 == 0:
        print(f"{number} * {m} = {result}")


   
