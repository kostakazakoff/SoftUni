def forecast(*args):
    locations = {"Sunny": [], "Cloudy": [], "Rainy": []}
    output = ''

    [locations[a[1]].append(a[0]) for a in args]

    for weather, locs in locations.items():
        for l in sorted(locs):
            output += f'{l} - {weather}\n'

    return output

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))