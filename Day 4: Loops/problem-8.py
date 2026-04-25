number = input("Enter a number: ")
number = int(number)
sum = 0
for number in range (1,number +1, 1):
    inverse = 1/number
    sum = sum + inverse
print(sum)