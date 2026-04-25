
number = input("Enter a number ")
number = int(number)
prime = True
prime = False
for factor in range(2,number): 
        if number % factor == 0:
           prime = False 
if prime == True:
    print("The number is prime")
else:
    print("The number is not prime")
