year = input("Please enter your birth year ")
year = int(year)

age = 2025 - year 
print(f"{age}")
if age < 10:
    print("Too young! Time travel is dangerous!")
elif age > 10 and age <= 100:
    print("Welcome, time traveler!")
else:
    print("Wow! You must be from another era!")        
