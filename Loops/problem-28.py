number = int(input("Number: "))
m = 0
n = 0
count_1 = 0
count_2 = 0
for number in range(1,number+1,1):
   
    if number % 5 == 0:
        count_1 = count_1 + 1
    elif number % 7 == 0:
        count_2 = count_2 + 1
print(f"Multiples of 5: {count_1}")    
print(f"Multiples of 7: {count_2}")
    


    