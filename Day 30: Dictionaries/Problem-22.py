students = ['Alice', 'Bob']
ages = [20, 22]
subjects = [['Math', 'Science'], ['English', 'History']]
d = {}

for a in range(0,len(students)):
    student_name = students[a]
    student_age = ages[a]
    student_subject = subjects[a]
    d[student_name] = {"age": student_age, "subject": student_subject}

print(d) 