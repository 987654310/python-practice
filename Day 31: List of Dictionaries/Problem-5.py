movies = [
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "reviews": 1200},
    {"title": "3 Idiots", "genre": "Drama", "rating": 8.5, "reviews": 950},
    {"title": "Bahubali", "genre": "Action", "rating": 8.2, "reviews": 1150},
    {"title": "Dangal", "genre": "Sports", "rating": 8.6, "reviews": 980},
    {"title": "KGF", "genre": "Action", "rating": 7.8, "reviews": 890},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "reviews": 1300},
    {"title": "PK", "genre": "Comedy", "rating": 8.1, "reviews": 860},
    {"title": "Jawan", "genre": "Action", "rating": 7.5, "reviews": 700},
    {"title": "Chhichhore", "genre": "Drama", "rating": 8.3, "reviews": 730},
    {"title": "The Kashmir Files", "genre": "Drama", "rating": 8.0, "reviews": 900}
]

for y in movies:
    if y["genre"] == "Sci-Fi" and y["reviews"] > 1000 and y["rating"] > 8.5:
        print(y) 
print("--------------------")
for x in movies:
    if x["genre"] == "Action" and x["reviews"] > 800 and x["rating"] < 8.0:
        print(x) 
