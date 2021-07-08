pizzas = ['margerita', 'calzone', 'four cheeses']
friend_pizzas = pizzas[:]
pizzas.append('mushroom')
friend_pizzas.append('vegetarian')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
