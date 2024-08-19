# bot.py

from chatterbot import ChatBot

chatbot = ChatBot("Chatbot")

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("You: ")
    if query in exit_conditions:
        break
    else:
        print(f"🤖 {chatbot.get_response(query)}")