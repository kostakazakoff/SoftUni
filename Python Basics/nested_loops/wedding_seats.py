last_sector = input()
first_sector_rows = int(input())
odd_rows_seats = int(input())
rows = first_sector_rows - 1
all_seats = 0

for sector in range(65, ord(last_sector) + 1):
    rows += 1
    for row in range(1, rows + 1):
        seats = odd_rows_seats
        if row % 2 == 0:
            seats = odd_rows_seats + 2
        all_seats += seats
        for seat in range(97, seats + 97):
            print(f'{chr(sector)}{row}{chr(seat)}')
print(all_seats)