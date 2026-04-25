students_in_classA = {"Alice", "Bob", "Charlie", "David"}
students_in_classB = {"Eve", "Frank", "Charlie", "Bob"}

d = students_in_classA - students_in_classA.intersection(students_in_classB)

print(d)