sum = 0

for number in range (0,20,1):
    if number%3 == 0:
        sum = sum + number
print(sum)

    
#Dry Run
#sum=0
#1>= 0 True
#1<= 20 True
#1%3 == 0 False
#...
#sum=0
#3>= 0 True
#3<= 20 True
#3%3 == 0 True
#3+0=3
#sum=3
#...
#6>= 0 True
#6<= 20 True
#6%3 == 0 True
#6+3 = 9
#sum = 9