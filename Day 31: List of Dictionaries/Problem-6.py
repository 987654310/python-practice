learners = [
    {"name": "Varun", "course": "Python", "completed": 95, "certified": True},
    {"name": "Shreya", "course": "JavaScript", "completed": 82, "certified": False},
    {"name": "Nikhil", "course": "React", "completed": 100, "certified": True},
    {"name": "Meghna", "course": "Python", "completed": 60, "certified": False},
    {"name": "Aakash", "course": "Java", "completed": 45, "certified": False}, 
    {"name": "Tanvi", "course": "Python", "completed": 89, "certified": True},
    {"name": "Riya", "course": "JavaScript", "completed": 55, "certified": False},
    {"name": "Zaid", "course": "Java", "completed": 97, "certified": True},
    {"name": "Ishita", "course": "React", "completed": 75, "certified": False},
    {"name": "Pranav", "course": "Java", "completed": 85, "certified": True}
]

for a in learners:
    if a["completed"] >= 90 and a["certified"] == False:
        print(a) 
print("--------------------")
for b in learners:
    if b["completed"] > 80 and b["certified"] == True:
        print(b) 