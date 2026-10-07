intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
        "response": "Hello! Nice to meet you. How can I help you?"
    },

    "help": {
        "patterns": ["help", "help me", "can you help me", "i need help"],
        "response": "Sure! You can ask me questions and I will try to help you."
    },

    "small_talk": {
        "patterns": [
            "how are you",
            "how are you doing",
            "what are you doing",
            "how is your day"
        ],
        "response": "I am doing great! Thanks for asking."
    },

    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "exit"],
        "response": "Goodbye! Have a nice day."
    }
}