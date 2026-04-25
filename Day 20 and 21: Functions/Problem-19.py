def calculate_grade(grade):
    score = "F"
    if grade > 89:
        score = "A"
    if grade > 79 and grade < 90:
        score = "B"
    if grade > 69 and grade < 80:
        score = "C"
    if grade > 59 and grade < 70:
        score = "D"
    return score

score = calculate_grade(85)
print(score)