number_1 = input("Please enter a number ")
number_2 = input("Please enter another number ")
number_3 = input("Please enter the final number ")

number_1 = int(number_1)
number_2 = int(number_2)
number_3 = int(number_3)

if number_1 > number_2 and number_3:
    print(f"The largest number is {number_1}")
elif number_2 > number_3 and number_1:
    print(f"The largest number is {number_2}") 
else:
    print(f"The largest number is {number_3}")       