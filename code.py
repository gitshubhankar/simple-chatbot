import nltk
from nltk.chat.util import Chat, reflections

# Ensure required NLTK data is downloaded
nltk.download('punkt')
nltk.download('wordnet')

# Define the pairs for pattern matching
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello|yo|whats up|sup|namaste|namaskar",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you. You can call me Bot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem.",]
    ],
    [
        r"I am fine",
        ["Great to hear that!",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon!",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I am just a program, so I don't have a physical location. But I'm here to help you wherever you are!",]
    ],
    [
        r"(.*) created you?",
        ["I was created by a programmer using Python and NLTK.",]
    ],
    [
        r"(.*) help (.*)",
        ["I can help you with a variety of tasks. How can I assist you today?",]
    ],
]

# Define a chatbot
def chatbot():
    print("Hi, I'm the chatbot you created. How can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
