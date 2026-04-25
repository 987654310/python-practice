string = "mississippi"

dictionary = {}

for a in string:
    if a in dictionary:
        dictionary[a] = dictionary[a] + 1
    else:
        dictionary[a] = 1 
print(dictionary)