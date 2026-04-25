string = input("Enter Password: ")
letter = False
num = False
for a in string:
    if a.isalpha():
        letter = True
    if a.isdigit():
        num = True

if len(string) > 4: 
    if letter == True and num == True:
        print("Valid")
else:
    print("Invalid")
    