from math import floor


def point_distance_from_zero(p: list):
    x = p[0]
    y = p[1]
    return abs(x) ** 2 + abs(y) ** 2


def line(line: list):
    p1 = line[0]
    p2 = line[1]
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    if point_distance_from_zero(p2) < point_distance_from_zero(p1):
        vector = [(floor(x2), floor(y2)), (floor(x1), floor(y1))]
    else:
        vector = [(floor(x1), floor(y1)), (floor(x2), floor(y2))]
    length = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2
    return vector, length


def longer_line(line1, line2: list):
    line1_vector, line1_length = line(line1)
    line2_vector, line2_length = line(line2)
    if line1_length >= line2_length:
        return f'{line1_vector[0]}{line1_vector[1]}'
    return f'{line2_vector[0]}{line2_vector[1]}'


points = []
for _ in range(4):
    point = []
    for _ in range(2):
        xy = float(input())
        point.append(xy)
    points.append(point)

l_1 = [points[0], points[1]]
l_2 = [points[2], points[3]]

print(longer_line(l_1, l_2))
