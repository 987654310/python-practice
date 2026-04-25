students = {
    "Alice": ["Math", "Science"],
    "Bob": ["English"],
    "Charlie": ["History", "Math"]
}
new_subject = "Physical Education"
l = len(students)

for k,v in students.items():
    students[k].append(new_subject)
print(students)