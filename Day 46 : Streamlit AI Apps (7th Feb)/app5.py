from google import genai

client = genai.Client(api_key = "AIzaSyCJu7AnPfA0PaZr0YfhHT1jhKREIgGbRnw")

def ask_gemini(question):
    response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = question,
    )
    return response.text
#------------------------------------

print("Welcome to Intelligent Personal Finance Manager! Type 'exit' to quit.")

monthly_income = input("Enter your monthly income after taxes: ")

print("Enter your recurring monthly expenses (type 'done' when finished):")

while True:
    m_desc = input("Expense description : " )
    m_amou = input("Amount : ")
    if m_desc == "done":
        goal = input("Enter your savings goal for this month : ")
        
        #print("Enter your daily expenses (type 'done' when finished):")



