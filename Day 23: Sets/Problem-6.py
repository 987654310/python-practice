set_a = {"apple", "banana", "cherry"}
set_b = {"cherry", "date", "fig"}

a = set_a.union(set_b)
b = set_a & set_b

c = set_a - b

print(f"Union of sets: {a}")
print(f"Intersection of sets: {b}")

print(f"Updated set_a: {c}")



