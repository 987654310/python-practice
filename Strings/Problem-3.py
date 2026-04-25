string = input("Enter Password: ")
letter = False
number = False
for a in string:
    if a.isalpha():
        letter = True
    if a.isdigit():
        number = True

if letter == True and number == True:
    print("Valid")
else:
    print("Invalid")