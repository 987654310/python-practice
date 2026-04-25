from google import genai

client = genai.Client(api_key = "AIzaSyCJu7AnPfA0PaZr0YfhHT1jhKREIgGbRnw")

def ask_gemini(question):
    response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = question,
    )
    return response.text
#------------------------------------
intructions = print("Welcome to Math Tutor! Type 'exit' to quit")

while True:
    
    problem = input("Enter a math problem (e.g., 'What is 5 plus 7?') : ")
    
    prompt = f'''Act as a math tutor, and answer the student's {problem}.'''
    
    if problem == "exit":
        print("Keep practicing math!")
        break

    ai_response = ask_gemini(prompt)
    print(f"Gemini AI : {ai_response}")
