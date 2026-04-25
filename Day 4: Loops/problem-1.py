number = input("Enter a number: ")
number = int(number)
sum = 0
for i in range (2,number + 1,2):
    square = i ** 2
    sum = sum + square
#    print(number)

print(f"Sum of squares of even numbers is {sum}")
    