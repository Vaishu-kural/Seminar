print("Hello! I am a Python Chatbot.")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I am fine! What about you?")

    elif user == "what is python":
        print("Bot: Python is a popular programming language used for AI, web, and automation.")

    elif user == "who created python":
        print("Bot: Python was created by Guido van Rossum.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")



