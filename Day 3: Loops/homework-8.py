number = input("Enter a number: ")
number = int(number)

start = 1
factorial = 1

while (start <= number):
    factorial = start * factorial
    start = start+1

print(f"The factorial is {factorial}")    


#Example input = 3
#start = 1
#factorial = 1
#1 <= 3 True
#   1 + 1 = 2
#   start = 2
#   factorial = 1
#   1 * 2 = factorial = 2
# print = 2 * 1 = 2
#   2<= 3 True
#   2 + 1 = 3
#   start = 3
#   2 * 3 = 6
#   factorial = 6
#print = 3 * 2 = 6
