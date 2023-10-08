import random
import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
chatbot_responses = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"]),
    (r'what is your name', ["I'm just a chatbot, so I don't have a name. You can call me ChatGPT.", "I'm your friendly neighborhood chatbot!"]),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Farewell!']),
    (r'(.*)', ["I'm not sure I understand. Could you please rephrase that?", "Can you tell me more about that?"]),
]

# Create a chatbot
chatbot = Chat(chatbot_responses, reflections)

def main():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
