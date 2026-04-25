final_number = 0
n = int(input("n: "))
sum = 0

while n > 0:
    remainder = n % 10 
    final_number = final_number * 10 + remainder    # (0*10+4=4)
    n = n//10    # 1234//10 = 123
    sum = final_number + sum

print(sum)
