number_1 = input("Enter the first number ")
number_2 = input("Enter the second number ")
operation = input("Enter an operation ")



number_1 = int(number_1)
number_2 = int(number_2)



if operation == "+" :
    result = (number_1 + number_2)
    print(f"The result is {result}")
elif operation == "-" :
    result = (number_1 - number_2)
    print(f"The result is {result}")
elif operation == "*" :
    result = (number_1 * number_2)
    print(f"The result is {result}")
elif operation == "/" and number_2!=0 :
    result = (number_1/number_2)
    print(f"The result is {result}")
else:
    print(f"no answer")
