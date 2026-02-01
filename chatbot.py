import json
import random
from datetime import datetime

with open("intents.json") as file:
    data = json.load(file)

LOG_FILE = "chat_logs.txt"


def tokenize(text):
    return text.lower().split()


def log_chat(user, bot):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}]\nUser: {user}\nBot: {bot}\n\n")


def get_response(user_input):
    tokens = tokenize(user_input)
    best_score = 0
    best_response = None

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern_tokens = tokenize(pattern)

            score = len(set(tokens) & set(pattern_tokens))

            if score > best_score:
                best_score = score
                best_response = random.choice(intent["responses"])

    if best_score == 0:
        return "Sorry, I didn’t quite get that. Could you rephrase?"

    return best_response


print("\nCustomer Service Chatbot Started (type 'quit' to exit)\n")

while True:
    user = input("You: ")

    if user.lower() == "quit":
        print("Bot: Goodbye!")
        break

    bot = get_response(user)
    print("Bot:", bot)

    log_chat(user, bot)
