from intents import intents
from knowledgebase import knowledgebase


def get_response(user_input):

    user_input = user_input.lower().strip()

    # Check intents using pattern matching
    for intent_name, intent_data in intents.items():
        for pattern in intent_data["patterns"]:
            if pattern == user_input:
                return intent_name, intent_data["response"]

    # Check knowledge base
    if user_input in knowledgebase:
        return "knowledge", knowledgebase[user_input]

    # Unknown input
    return "unknown", "Sorry, I don't understand that yet."


print("=" * 45)
print("       SIMPLE RULE-BASED CHATBOT")
print("=" * 45)

print("\nBot: Hello! I am your chatbot.")
print("Bot: Type 'bye' to exit.\n")


# -------------------------
# CONVERSATION HISTORY
# -------------------------

history = []

while True:

    user_input = input("You: ")

    intent, response = get_response(user_input)

    print("Bot:", response)

    # Store conversation in history
    history.append(f"You: {user_input}")
    history.append(f"Bot: {response}")

    if intent == "goodbye":
        break


# -------------------------
# SAVE CONVERSATION HISTORY
# -------------------------

with open("conversation_history.txt", "w", encoding="utf-8") as file:

    for message in history:
        file.write(message + "\n")

print("\nConversation history saved successfully!")