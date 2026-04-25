d = {'m': 0, 'i': 0, 's': 0, 'p': 0}
string = "mississippi"
count = 0

for a in range(0,len(string)):
    if "m" in string[a]:
        count = count + 1
d["m"] = count
count = 0

for a in range(0,len(string)):
    if "i" in string[a]:
        count = count + 1
d["i"] = count
count = 0

for a in range(0,len(string)):
    if "s" in string[a]:
        count = count + 1
d["s"] = count
count = 0

for a in range(0,len(string)):
    if "p" in string[a]:
        count = count + 1
d["p"] = count


print(d)