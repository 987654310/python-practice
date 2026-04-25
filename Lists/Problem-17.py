list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = []

for a in range(0,len(list1)):
    num = list1[a]
    if num in list2:
        common_elements.append(num)
print(common_elements)