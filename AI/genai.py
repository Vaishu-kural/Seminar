import wikipedia

print("WikiBot Ready! Ask any question. Type 'bye' to exit.")

while True:
    question = input("You: ")

    if question.lower() == "bye":
        print("Bot: Goodbye! ")
        break

    try:
        answer = wikipedia.summary(question, sentences=2)
        print("Bot:", answer)
    except:
        print("Bot: Sorry, I couldn't find information on that.")
