snowballs = int(input())
best_value = 0
best_weight = 0
best_time = 0
best_quality = 0


class Snowball:
    def __init__(self, w, t, q):
        self.weight = w
        self.time = t
        self.quality = q
        self.value = int((w / t) ** q)


for i in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    sb = Snowball(weight, time, quality)
    if sb.value > best_value:
        best_value = sb.value
        best_weight = sb.weight
        best_time = sb.time
        best_quality = sb.quality

print(f'{best_weight} : {best_time} = {best_value} ({best_quality})')
