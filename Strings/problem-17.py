string = input("Enter Password: ")
#letter = False
number = False
for a in string:
    #if a.isalpha():
    #    letter = True
    if a.isdigit():
        number = True

if number == True: #and letter == False:
    print("Valid")
else:
    print("Invalid")