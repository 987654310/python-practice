km = input("Enter the number of kilometers to your destination: ")
km = int(km)

total_fare = 0
fare = 0

if km <= 5:
    fare = km * 10
    total_fare = fare + 50
elif km > 5:
    a = km - 5
    fare = a * 15
    total_fare = 50 + (5 * 10) + fare
print(f"₹{total_fare}")

