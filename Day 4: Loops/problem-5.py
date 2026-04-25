number = input("Enter a number: ")
number = int(number)
sum = 0
for number in range (1,number + 1,1):
    square = number ** 2
    sum = sum + square
#    print(number)
print(f"sum: {sum}")
    