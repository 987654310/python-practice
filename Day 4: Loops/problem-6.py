num = input("Enter a number: ")
num = int(num)
sum = 0
for num in range (1,num + 1,1):
    cube = num ** 3
    sum = sum + cube
    print(num)
print(f"Sum of cubes: {sum}")
