from google import genai

client = genai.Client(api_key = "AIzaSyCJu7AnPfA0PaZr0YfhHT1jhKREIgGbRnw")

def ask_gemini(question):
    response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = question,
    )
    return response.text
#------------------------------------
intructions = print("Welcome to Health and Wellness Coach! Type 'exit' to quit.")

while True:
    
    1 == input("Please enter your age : ")
    2 == input("Enter your weight (kg) : ")
    3 == input("Enter your height (cm) : ")
    4 == input("Select your fitness level (Beginner/Intermediate/Advanced) : ")
    5 == input("What are your health goals? (e.g., weight loss, muscle gain) : ")
    6 == input("Do you have any dietary preferences or restrictions? ")
    
    prompt = f'''Calculate the BMI, and suggest daily caloric needs for their goal: {4}, based on their age: {1}, based on their weight: {2}, based on their height: {3}, fitness level: {5}, and their dietary preferences or restrictions: {6}. Create a personalized plan based on all of this including excercise routines, mindful practices, and meal plans'''
    
    if input == "exit":
        print("Thank you for using Health and Wellness Coach! Stay healthy and mindful!")
        break

    ai_response = ask_gemini(prompt)
    print(f"Gemini AI : {ai_response}")

    print("Would you like to make any changes or get alternative suggestions? (yes/no) : ")
    response = input("Your request : ")
    if response == "exit":
        print("Thank you for using Health and Wellness Coach! Stay healthy and mindful!")
        break

    prompt_2 = (f"There is an additional request, make changes in occordance to it: {response}")
    
    AI_response = ask_gemini(prompt_2)
    print(f"Gemini AI : {AI_response}")

    response_2 = input("Is this acceptable? (yes/no) : ")
    if response_2 == "exit":
        print("Thank you for using Health and Wellness Coach! Stay healthy and mindful!")
        break
    if response_2 == "no":
        prompt_3 = ("Make futher changes since changes made in occordance to the request didn't satisfy the requests")
        AI_response_2 = ask_gemini()
        print(f"Gemini AI : {AI_response_2}")
    
    while response_2 != "exit":
        log = input("Would you like to log today's activities or meals? (yes/no) : ")
        if "yes":
            meals = input("Enter your meals for today: ")
            activities = input("Enter your activities for today: ")
            calander = (f"Create a written calendar including activities: {activities} and meals: {meals}")
            AI_response_calendar = ask_gemini()
            print(f"Gemini AI : {AI_response_calendar}")
        if "no":
            while meals and activities != "exit":
                progress = input("Do you want to continue or exit? (continue/exit): exit")
                if progress == "exit":
                    print("Thank you for using Health and Wellness Coach! Stay healthy and mindful!")
                    exit(0)
                else:
                    final_response = input("If you have any more questions and concerns, please enter them here or enter exit if you wish to leave:")
                    if final_response == "exit":
                        print("Thank you for using Health and Wellness Coach! Stay healthy and mindful!")
                        exit(0)
                    else:
                        final_prompt = (f"Please adrress these questions or responses: {final_response}")
                        final_AI_response = ask_gemini()
                        print(f"Gemini AI : {final_AI_response}")
                        print("Thank you for using Health and Wellness Coach! Stay healthy and mindful!")

    


######





#Welcome to Health and Wellness Coach! Type 'exit' to quit.

# Please enter your age: 30
# Enter your weight (kg): 70
# Enter your height (cm): 175
# Select your fitness level (Beginner/Intermediate/Advanced): Beginner
# What are your health goals? (e.g., weight loss, muscle gain): Weight loss and stress reduction
# Do you have any dietary preferences or restrictions? Vegetarian

# Gemini AI:
# - Calculated BMI: 22.9 (Normal weight)
# - Daily Caloric Needs: Approximately 2,200 calories
# - Suggested Caloric Intake for Weight Loss: 1,700 calories

# Here's your personalized plan:

# Exercise Routine:
# - Monday: 30-minute brisk walk, 15-minute yoga session
# - Wednesday: 20-minute cycling, 10-minute meditation
# - Friday: 30-minute swimming, 15-minute stretching

# Meal Plan:
# - Breakfast: Oatmeal with fruits and nuts
# - Lunch: Quinoa salad with mixed vegetables
# - Dinner: Grilled tofu with steamed broccoli and brown rice
# - Snacks: Carrot sticks with hummus, apple slices

# Mindfulness Practice:
# - Daily 10-minute guided meditation before bedtime

# Would you like to make any changes or get alternative suggestions? (yes/no): yes

# Your request: I don't have access to a pool. Can you suggest a different exercise for Friday?

# Gemini AI:
# Sure! How about a 30-minute dance cardio session instead of swimming?

# Is this acceptable? (yes/no): yes

# Would you like to log today's activities or meals? (yes/no): no

# Do you want to continue or exit? (continue/exit): exit

# Thank you for using Health and Wellness Coach! Stay healthy and mindful!
