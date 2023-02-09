wins = 0
drawn = 0
loses = 0
for i in range(3):
    result = input()
    if result[0] > result[2]:
        wins += 1
    elif result[0] == result[2]:
        drawn += 1
    else:
        loses += 1
print(f'Team won {wins} games.')
print(f'Team lost {loses} games.')
print(f'Drawn games: {drawn}')