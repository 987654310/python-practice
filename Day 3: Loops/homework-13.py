
sum = 0
count = 0
average = 0
for number in range (1,101,1):
    if number%2 == 0:
          count = count +1
          sum = sum + number
print(sum/count)





# Dry Run
# 1 >= 0 and 1 <= 100 True
# 1%2 == 0 False 
# sum = 0
# count = 0
# average = 0
#...
# 2 >= 0 and 2 <= 100 True
# 2%2 == 0 True
# sum = 2
# count = 1
# average = 2
# ...
# 4 >= 0 and 4 <= 100 True
# 4%2 == 0 True
# count = 2
# sum = 6
# average = 3
#...