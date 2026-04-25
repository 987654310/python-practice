english_speakers = {"John", "Emma", "Sophia", "Michael"}
french_speakers = {"Emma", "Lucas", "Sophia", "Chloe"}

symmetric_difference_set = english_speakers.symmetric_difference(french_speakers)
intersection_set = english_speakers.intersection(french_speakers)

print(f"These are the people who speak only one language: {symmetric_difference_set}")
print(f"These are the people who can speak two languages: {intersection_set}")