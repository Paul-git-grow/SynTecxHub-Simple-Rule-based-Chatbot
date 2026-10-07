# Simple Rule-Based Chatbot

## Project Overview

This project is a Simple Rule-Based Chatbot developed using Python.

The chatbot uses pattern matching to identify user intents and provides predefined rule-based responses. It also contains a small knowledge base for answering domain-related questions and stores the conversation history.

## Objective

The objective of this project is to:

- Create a conversational chatbot using pattern matching
- Support intents such as greeting, help, and small talk
- Provide rule-based responses
- Answer domain-related questions using a knowledge base
- Provide an interactive console interface
- Store conversation history

## Technologies Used

- Python
- Pattern Matching
- Rule-Based AI

## Project Structure

```text
Simple-Rule-Based-Chatbot/
│
├── main.py
├── intents.py
├── knowledge_base.py
├── conversation_history.txt
└── README.md
```

## Features

### 1. Pattern Matching
The chatbot compares user input with predefined patterns to identify the appropriate intent.

### 2. Intents
The chatbot supports:

- Greeting
- Help
- Small Talk
- Goodbye

### 3. Rule-Based Responses
Each intent contains predefined responses that are displayed when a matching pattern is found.

### 4. Knowledge Base
The chatbot can answer simple domain-related questions about:

- Artificial Intelligence
- Python
- Machine Learning
- Chatbots
- Rule-Based Systems

### 5. Interactive Console
Users can communicate with the chatbot directly through the Python console.

### 6. Conversation History
The conversation between the user and chatbot is stored in:

```text
conversation_history.txt
```

## Example

```text
Bot: Hello! I am your chatbot.

You: hi
Bot: Hello! Nice to meet you. How can I help you?

You: what is python
Bot: Python is a high-level programming language known for its simple syntax and wide range of applications.

You: how are you
Bot: I am doing great! Thanks for asking.

You: bye
Bot: Goodbye! Have a nice day.

Conversation history saved successfully!
```

## How to Run

Open the project folder in a terminal and run:

```bash
python main.py
```

Type `bye` to end the conversation.

## Conclusion

This project demonstrates a basic rule-based chatbot using pattern matching, intents, predefined responses, a small knowledge base, and conversation history logging.