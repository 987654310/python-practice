dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
d = {}

for k,v in dict1.items():
        d[k] = v
for k,v in dict2.items():
        d[k] = v
print(d)