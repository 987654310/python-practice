string = input("Enter a word: ")
letter = input(f"Enter a letter to remove from {string}: ")
output = ""

for a in string:
    if letter != a:
        output = output + a
print(output)