list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
d = {}

for a in list_with_duplicates:
    if a not in d:
        d[a] = a

d_list = list(d)

print(d_list)