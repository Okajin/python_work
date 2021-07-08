person_0 = {'first name': 'florient', 'last name': 'michel', 'age': 36, 'city': 'Halluin'}
person_1 = {'first name': 'seb', 'last name': 'ddl', 'age': 33, 'city': 'Tourcoing'}
person_2 = {'first name': 'sedo', 'last name': 'kun', 'age': 35, 'city': 'Avignon'}

people = [person_0, person_1, person_2]

for person in people:
    print(f"The people is named {person['first name'].title()} {person['last name'].title()}, he or she lives in {person['city']} and is {person['age']} old")
    print("{} {} is {} years old and lives in {}".format(person['first name'].title(), person['last name'].title(), person['age'], person['city']))
