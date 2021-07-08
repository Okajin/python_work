guests = ['Einstein', 'Newton', 'Hawking']
message = f"Hello {guests[0]}, would you like to have a dinner?"
print(message)
message = f"Hello {guests[1]}, would you like to have a dinner?"
print(message)
message = f"Hello {guests[2]}, would you like to have a dinner?"
print(message)
print(f"\nUnfortunately, {guests[1]} can't come\n")
guests[1] = 'Stark'
message = f"Hello {guests[0]}, would you like to have a dinner?"
print(message)
message = f"Hello {guests[1]}, would you like to have a dinner?"
print(message)
message = f"Hello {guests[2]}, would you like to have a dinner?"
print(message)
message = f"\nHello {guests[0]}, I found a bigger table, let's invite some new people!"
print(message)
message = f"Hello {guests[1]}, I found a bigger table, let's invite some new people!"
print(message)
message = f"Hello {guests[2]}, I found a bigger table, let's invite some new people!"
print(message)
guests.insert(0, 'Thor')
message = f"\nHello {guests[0]}, would you like to have a dinner?"
print(message)
guests.insert(2, 'Odin')
message = f"Hello {guests[2]}, would you like to have a dinner?"
print(message)
guests.append('Heimdall')
message = f"Hello {guests[-1]}, would you like to have a dinner?"
print(message)
