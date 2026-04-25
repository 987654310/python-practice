string = "hello there world"
output = ""
words = string.split()

for a in range(0,len(words)):
    if a == 0:
        output = output + " " + words[a].capitalize()
    elif a == len(words) - 1:
        output = output + " " + words[a].capitalize()
    else:
        output = output + " " + words[a]
print(output)