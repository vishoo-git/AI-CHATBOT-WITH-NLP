import nltk
from nltk.chat.util import Chat, reflections

# Download necessary resources
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! How can I help?"]),
    (r"my name is (.*)", ["Hello %1, nice to meet you!", "Hi %1, how can I help you?"]),
    (r"(.*) your name?", ["I'm a chatbot, I don't have a name, but you can call me Bot!"]),
    (r"how are you?", ["I'm doing great, thank you for asking!", "I'm just a bot, but I'm here to help you!"]),
    (r"(.*) (help|support)", ["I'm here to assist you. How can I help you today?"]),
    (r"quit|exit|bye", ["Goodbye! Have a great day!", "Bye! It was nice talking to you!"]),
    (r"(.*)", ["I'm not sure how to respond to that, but feel free to ask me anything else!"])
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def chat():
    print("Hello! Type 'quit' or 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Bot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Bot:", response)

# Start the chatbot
if __name__ == "__main__":
    chat()
