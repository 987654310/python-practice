n = input("n: ")
n = int(n)
t = input("t: ")
t = int(t)

count = 0
for number in range(1,n + 1):
    if number > t:
        count = count + 1

print(f"Count : {count}")

#n = 15
#t = 10
#count = 1
#10 > 15 false
# 11 > 15 false




   