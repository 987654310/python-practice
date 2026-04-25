sentence = "hello world hello"
s = sentence.split()
dictionary = {}

for a in s:
    if a in dictionary:
        dictionary[a] = dictionary[a] + 1
    else:
       dictionary[a] = 1
print(dictionary)

