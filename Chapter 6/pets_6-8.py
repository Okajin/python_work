pet_0 = {'kind': 'lizard', 'owner': 'florient'}
pet_1 = {'kind': 'cat', 'owner': 'elodie'}
pet_2 = {'kind': 'dog', 'owner': 'seb'}
pet_3 = {'kind': 'monkey', 'owner': 'sedo'}
pet_4 = {'kind': 'parrot', 'owner': 'faerie'}

pets = [pet_0, pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"{pet['owner'].title()} owns a {pet['kind']}")
