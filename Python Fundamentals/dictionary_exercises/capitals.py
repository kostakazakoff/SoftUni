countries = input().split(', ')
cities = input().split(', ')
capitals = zip(countries, cities)
capitals = {country: city for country, city in capitals}
for country, city in capitals.items():
    print(f'{country} -> {city}')