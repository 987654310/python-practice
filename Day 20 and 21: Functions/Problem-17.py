def multiply_list(num):
    m = 1
    for a in range(len(num)):
        m = m * num[a]
    return m

m = multiply_list([1, 2, 3, 4])
print(m)