def process_messages(messages, sent_messages):
    while messages:
        processed_message = messages.pop()
        sent_messages.append(processed_message)

def show_messages(sent_messages):
    for message in sent_messages:
        print(message)

chat = ["hi!", "how are you?", "fine!"]
sent_chat = []

process_messages(chat[:], sent_chat)
show_messages(sent_chat)
print(chat)