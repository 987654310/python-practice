original_dict = {'a': 1, 'b': 2, 'c': 3}
output = {}

for k, v in original_dict.items():
    output[v] = k
print(output)
#print(original_dict[::-1])