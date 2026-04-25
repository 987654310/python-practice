def functions(scores, attendance):
    original = attendance
    original_2 = scores
    l = len(scores)
    count = 0
    average = 0
    sum = 0

    print(scores)
    
    for a in range(0,len(scores)):
        sum = sum + scores[a]
    average = sum/l
    
    print(average)

    if average >= 85:
        for a in range(0,len(scores)):
            scores[a] = scores[a] + 2
    ##
    for a in range(0,len(attendance)):
        if original[a] >= 90:
            scores[a] = scores[a] + 5
    print("line 14 ",scores)

    for a in range(0,len(scores)):
        if original_2[a] < 40:
            count = count + 1
        
        if count == 0:
            scores[a] = scores[a] + 3
    print(scores)

    for a in range(0,len(scores)):
        if scores[a] > 100:
            scores[a] = 100
    return scores, average 
    
scores, average = functions([85, 92, 78, 88, 95], [95, 88, 92, 85, 90])
print(f"Final Grades: {scores}, Class Average: {average}")

#Final grades: [92, 97, 83, 93, 100]
#Final grades: [45, 63, 35, 75, 55]