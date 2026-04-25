list1 = ["Hello", "Good"]
list2 = ["World", "Morning"]
list3 = []

for a in range(0,len(list1)):
    combine = list1[a] + list2[a]
    list3.append(combine)
print(list3)
