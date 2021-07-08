animals = ['lizard', 'snake', 'chameleon', 'turtles', 'gecko', 'crocodiles']
print("The first three items in the list are:")
for animal in animals[:3]:
    print(animal.title())
print("\nThree items in the middle of the list are:")
for animal in animals[2:-1]:
    print(animal.title())
print("\nThe last three items of the list are:")
for animal in animals[3:]:
    print(animal.title())
