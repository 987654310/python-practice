number = input("Number:")
number = int(number)
start = 1
end = 10
table = number
while(start<=10): 
    print(f"{number} x {start} = {table}")
    start = start+1
    table = start * number 


    #Example input = 2
    #Start = 0
    #End = 10
    #Table = 0
    #0 <= 10 True
    #0+1 =1
    #1 * 5 = 5
    #table = 5
    #1 <= 10 True
    #1+1 =2
    #2 * 5 = 10...