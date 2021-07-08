cities = {
    'tokyo': {
        'country': 'Japan',
        'population': '37.3 million',
        'fact': 'Best City',
    },

    'nantes': {
        'country': 'France',
        'population': '321 thousands',
        'fact': 'Future work',
    },

    'los angeles': {
        'country': 'USA',
        'population': '12.7 million',
        'fact': 'city of angels',
    },
}

for city, details in cities.items():
    characteristics = f"{details['country']}, has {details['population']} inhabitants and is my {details['fact']}!"
    print(f"\n{city.title()} is in {characteristics}")
