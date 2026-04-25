def generate_multiplication_table(x):
    for y in range(1,11,1):
        m = x * y
        print(f"{x} x {y} = {m}")

generate_multiplication_table(5)
