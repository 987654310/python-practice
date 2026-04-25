books = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "year": 1988, "available": True},
    {"title": "Atomic Habits", "author": "James Clear", "year": 2018, "available": False},
    {"title": "Sapiens", "author": "Yuval Noah Harari", "year": 2011, "available": True},
    {"title": "1984", "author": "George Orwell", "year": 1949, "available": True},
    {"title": "Ikigai", "author": "Héctor García", "year": 2016, "available": False},
    {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "year": 1997, "available": True},
    {"title": "Wings of Fire", "author": "A. P. J. Abdul Kalam", "year": 1999, "available": True},
    {"title": "Thinking Fast and Slow", "author": "Daniel Kahneman", "year": 2011, "available": False},
    {"title": "The Power of Now", "author": "Eckhart Tolle", "year": 1997, "available": True},
    {"title": "The Secret", "author": "Rhonda Byrne", "year": 2006, "available": True}
]

for a in books:
    if a["available"] == True:
        print(a)
print("---------")
for b in books:    
    if b["year"] > 2000:
        print(b)