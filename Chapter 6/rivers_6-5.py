rivers = {
    'nile': 'egypt',
    'mississipi': 'usa',
    'seine': 'france',
}

for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}")

for river in rivers.keys():
    print(f"{river.title()}")

for country in rivers.values():
    print(f"{country.title()}")
