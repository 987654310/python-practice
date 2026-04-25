string = "hello world"

d = {"a":0,"e":0,"i":0,"o":0,"u":0}

for a in string:
    if a in d:
        d[a] = d[a] + 1
print(d)