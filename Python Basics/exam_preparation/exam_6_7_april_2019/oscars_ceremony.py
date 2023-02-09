hall_rent = int(input())
statuette = hall_rent * 0.7
katering = 0.85 * statuette
sound = katering / 2
total = hall_rent + statuette + katering + sound
print(f'{total:.2f}')