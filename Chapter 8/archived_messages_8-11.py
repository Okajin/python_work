short_messages = ['Hello', 'Nice time', 'Good Game', 'See you']
sent_messages = []


def send_message(short_messages, sent_message):
    while short_messages:
        current_message = short_messages.pop()
        print(f"Sending the message: {current_message}")
        sent_messages.append(current_message)


def show_sent_messages(sent_messages):
    print("\nThe following messages have been sent: ")
    for sent_message in sent_messages:
        print(sent_message)


send_message(short_messages[:], sent_messages)
show_sent_messages(sent_messages)
print(short_messages)
