t1 = (1, 2, 70)
t2 = (11, 12, 4)

sum_of_t1 = 0
sum_of_t2 = 0

for a in t1:
    sum_of_t1 = sum_of_t1 + a

for b in t2:
    sum_of_t2 = sum_of_t2 + b


if sum_of_t2 > sum_of_t1:
    print("t2 is greater than t1")

else:
    print("t1 is greater than t2")