final_number = 0
N = int(input("N: "))
N_1 = N
Original_N = N



num_digit = 0

while N > 0:
    N = N//10
    num_digit = num_digit + 1

while N_1 > 0:
    remainder = N_1%10
    final_number=final_number+(remainder ** num_digit )
    N_1 = N_1//10
    #print(number_multiplied)

print(final_number)

if final_number == Original_N:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")    

    
        

    






