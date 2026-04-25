original_list = [1,2,3,4,5]
new_list = []
for a in range(len(original_list)-1,-1,-1):
    new_list.append(original_list[a])
print(new_list) 