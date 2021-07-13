short_messages = ['Hello', 'Nice time', 'Good Game', 'See you']
sent_messages = []

while short_messages:
    current_message = short_messages.pop()
    print(f"Sending the message: {current_message}")
    sent_messages.append(current_message)

print("\nThe following messages have been sent: ")
for sent_message in sent_messages:
    print(sent_message)

print(f"\n{short_messages}")
