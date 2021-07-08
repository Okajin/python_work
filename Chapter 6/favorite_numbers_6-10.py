favorite_numbers = {
    'florient': {
        'number1': 13,
        'number2': 25,
    },

    'elodie': {
        'number1': 3,
        'number2': 6,
    },

    'seb': {
        'number1': 42,
        'number2': 1010,
    },

    'faerie': {
        'number1': 27,
        'number2': 54,
    },

    'sedokun': {
        'number1': 46,
        'number2': 2,
    },
}

for people, number in favorite_numbers.items():
    fav_number = f"{number['number1']} and {number['number2']}"
    print(f"\n{fav_number} are {people.title()}'s favorite numbers")
