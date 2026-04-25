n = input("n: ")
n = int(n)

m = input("m: ")
m = int(m)

multiple = 0
sum = 0

for num in range(1,n + 1):
    if num % m == 0:    
        sum = sum + num
print(sum)
    
    
    
    
   # multiple = num * m
   # print(f"{m} * {num} = {multiple}")
   
