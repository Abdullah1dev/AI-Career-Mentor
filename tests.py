from chatbot import AICareerMentor
from config import Config

print("GEMINI_API_KEY loaded:", bool(Config.GEMINI_API_KEY))
print("GEMINI_API_KEY length:", len(Config.GEMINI_API_KEY) if Config.GEMINI_API_KEY else 0)


mentor = AICareerMentor()

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = mentor.chat(user_input)
    print(f"\nAI Career Mentor: {response}\n")