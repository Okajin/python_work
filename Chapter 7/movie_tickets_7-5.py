prompt = "\nPlease enter your age:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    elif int(age) < 4:
        print(f"At {age} the ticket is free")
    elif int(age) > 3 and int(age) < 13:
        print(f"At {age} the ticket costs $10")
    elif int(age) > 12:
        print(f"at {age} the ticket costs $15")
