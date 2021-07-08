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
