students = [
    {"name": "Aarav", "class": "10A", "attendance": 92},
    {"name": "Kiara", "class": "10A", "attendance": 85},
    {"name": "Aryan", "class": "10B", "attendance": 67},
    {"name": "Ishaan", "class": "10A", "attendance": 76},
    {"name": "Diya", "class": "10C", "attendance": 98},
    {"name": "Vivaan", "class": "10B", "attendance": 81},
    {"name": "Meera", "class": "10C", "attendance": 55},
    {"name": "Anika", "class": "10A", "attendance": 90},
    {"name": "Kavya", "class": "10B", "attendance": 61},
    {"name": "Rudra", "class": "10C", "attendance": 72}
]

for i in students:
    if i["class"] == "10A" and i["attendance"] > 90:
        print(i)
        print("--------------------")
for a in students:
    if a["attendance"] < 70:
        print(a)
        