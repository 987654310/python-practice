num = [4, -3, 7, -1, 0, 5]
for a in range(1,6): # or # for a in range(len(num)):
    if num[a] < 0:
        num[a]=0
print(num)
