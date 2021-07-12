sandwich_orders = ['cheese', 'eggs', 'veggie', 'yakisoba']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"\nI made a {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
