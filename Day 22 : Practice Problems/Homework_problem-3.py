def function(salary,experience,performance):
    original = salary[:]
    s = 0

    for a in range(len(salary)):
        if experience[a] >= 1 and experience[a] <= 3:
            salary[a] = salary[a] + (original[a]/100) * 10
        
        if experience[a] >= 4 and experience[a] <= 7:
            salary[a] = salary[a] + (original[a]/100) * 20
        
        if experience[a] >= 8:
            salary[a] = salary[a] + (original[a]/100) * 30
    print(salary)

    for a in range(len(salary)):
        if performance[a] == "A":
            salary[a] = salary[a] + (original[a]/100) * 15
        
        if performance[a] == "B":
            salary[a] = salary[a] + (original[a]/100) * 10

        if performance[a] == "C":
            salary[a] = salary[a] + (original[a]/100) * 5
    print(salary)
    
    for a in range(len(salary)):
        if salary[a] > 50000:
            salary[a] = salary[a] - (original[a]/100) * 10
    print(salary)

    for a in range(len(salary)):
        if "A" in performance:
            salary[a] = salary[a] + 2000
    print(salary)

    for a in range(0,len(salary)):
        s = s + salary[a]
    print(s)
    return salary, s    

salary, s = function([40000, 60000, 35000], [2, 5, 8], ['A', 'B', 'C'])
print(f"Final Salaries: {salary}, Total Exepense: {s}")