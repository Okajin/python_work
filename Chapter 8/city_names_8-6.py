def city_country(city_name, country):
    pair = f"{city_name}, {country}"
    return pair.title()


city_and_country = city_country("Santiago", "Chile")
print(city_and_country)
city_and_country = city_country("Paris", "France")
print(city_and_country)
city_and_country = city_country("Tokyo", "Japan")
print(city_and_country)
