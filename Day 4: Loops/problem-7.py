number = input("Enter a number: ")
number = int(number)

sum = 0
factorial = 1
for number in range(1,number +1,1):
    factorial = (number * factorial)
    sum = sum + factorial
print(f"The sum of factorials of {number} is {sum}")



# 4 factorial
#4!+3!+2!+1!
#24+6+2+1 = 33