list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
unique_num = []

for a in range(0,len(list1)):
    num = list1[a]
    if num not in list2:
        unique_num.append(num)
print(unique_num)
