words_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
d = {}

for a in words_list:
    if a in d:
        d[a] = d[a] + 1
    else:
       d[a] = 1

print(d)