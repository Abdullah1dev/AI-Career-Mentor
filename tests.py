from chatbot import AICareerMentor

mentor = AICareerMentor()

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = mentor.chat(user_input)
    print(f"\nAI Career Mentor: {response}\n")