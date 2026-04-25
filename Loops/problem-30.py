
final_number = 0
n = int(input("n: "))
n_1 = n

while n > 0:
    remainder = n%10
    final_number = final_number%10 + remainder
    n = n//10
    