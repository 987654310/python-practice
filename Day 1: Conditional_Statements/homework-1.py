grade = input("Enter your grade ")
grade = int(grade)

if grade<=100 and grade>=90 :
    print("A")
elif grade<90 and grade>=75 :
    print("B")
elif grade<75 and grade>=50 :
    print("C")
else:
    print("Fail")
