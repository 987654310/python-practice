num = input("Enter number: ")
num_int = int(num)
d = {}

for a in range(1,num_int+1):
    d[a] = a**3

print(d) 