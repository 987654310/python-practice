number = input("Number:")
number = int(number)
count_1 = 0
count_2 = 0
for number in range(1,number+1,1):
    if number % 2 == 0:
        count_1 = count_1 + 1
      
    else:
        count_2 = count_2 + 1

print(f"Even count: {count_1}")        
print(f"Odd count: {count_2}")    
