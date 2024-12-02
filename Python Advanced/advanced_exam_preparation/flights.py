import enum


def flights(*args):
    flights, k = {}, None
    for idx, info in enumerate(args):
        if idx % 2 == 0:
            if info == 'Finish': break
            k, v = info, 0
        else: v = info
        if k not in flights:
            flights.update({k: 0})
        flights[k] += v
    return flights


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0)) 