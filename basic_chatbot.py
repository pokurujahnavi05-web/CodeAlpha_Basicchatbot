
def chatbot():

    print("Welcome to My First Chatbot!")
    print("Type 'bye' to exit.")

    while True:
        message = input("You: ").lower().strip()

        if message == "hello":
            print("Bot: Hi! How can I help you?")

        elif message == "how are you":
            print("Bot: I'm fine, thanks!")

        elif message == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
