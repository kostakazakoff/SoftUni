men = int(input())
wimen = int(input())
tables = int(input())
tables_counter = 0

for m in range(1, men + 1):
    for w in range(1, wimen + 1):
        tables_counter += 1
        print(f'({m} <-> {w})', end = ' ')
        if tables_counter == tables:
            exit()