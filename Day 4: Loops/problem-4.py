final_number = 0
N = int(input("n: "))
N_1 = N

while N > 0:
    remainder = N%10 
    final_number = final_number*10 + remainder   
    N = N//10   

if final_number == N_1:
    print(f"Palindrome Number {N_1} reversed is {final_number}")  #print(final_number)
elif final_number != N_1:
    print(f"Not a Palindrome Number {N_1} reversed is {final_number}")   



#Dry Run

#final_number = 0
#N = 1561
#1561 > 0 True:

#1561/10 = 156 
#Remainder = 1
#0 * 10 = 0 
#0 + 1 = 1
#final_number = 1
#1561//10 = 156
#N = 156

#156 > 0 True:

#156/10 = 15 
#Remainder = 6
#1 * 10 = 10 
#10 + 6 = 16
#final_number = 16
#156//10 = 15
#N = 15

#15 > 0 True:

#15/10 = 1
#Remainder = 5
#16 * 10 = 160 
#160 + 5 = 165
#final_number = 165
#15//10 = 1
#N = 1

#1 > 0 True:

#1/10 = 0
#Remainder = 1
#165 * 10 = 1650
#1650 + 1 = 1651
#final_number = 1651
#//10 = 0
#N = 0

#0 > 0 False




