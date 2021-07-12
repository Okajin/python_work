sandwich_orders = ['cheese', 'pastrami', 'eggs', 'veggie', 'pastrami', 'yakisoba', 'pastrami']
finished_sandwiches = []

prompt = ("Sorry but we ran out of pastrami.")
print(prompt)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made a {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
