import re


def add_racer():
    global racers, name, score
    if name not in names:
        return
    if name not in racers:
        racers[name] = 0
    racers[name] += score


racers = {}
count = 1
extensions = ['st', 'nd', 'rd']
names = input().split(', ')

string = input()
while string != 'end of race':
    name = ''.join(re.findall(r'[A-Za-z]', string))
    score = re.findall(r'\d', string)
    score = sum(int(x) for x in score)
    add_racer()
    string = input()
racers = dict(sorted(racers.items(), reverse=True, key=lambda item: item[1]))
rank_list = [k for k in racers.keys()]
[print(f'{i + 1}{extensions[i]} place: {rank_list[i]}') for i in range(3)]
