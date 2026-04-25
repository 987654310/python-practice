def sum_of_list(num):
    sum = 0
    for a in range(len(num)):
        sum = sum + num[a]
    return sum

sum = sum_of_list([1, 2, 3, 4])
print(sum)