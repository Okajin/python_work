favorite_places = {
    'florient': {
        'place1': 'Tokyo',
        'place2': 'Nantes',
        'place3': 'Los Angeles',
    },

    'sedo': {
        'place1': 'Avignon',
        'place2': 'Golden Sand',
        'place3': 'Reach',
    },

    'ninie': {
        'place1': 'Stormwind',
        'place2': 'Darnassus',
        'place3': 'Ironforge',
    },
}

for people, place in favorite_places.items():
    print(f"\npeople: {people}")
    fav_place = f"{place['place1']}, {place['place2']} and {place['place3']}"
    print(f"\n{people.title()}'s favorite places are {fav_place}")
