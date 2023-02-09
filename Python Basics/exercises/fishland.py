skumria_kg = float(input())
caca_kg = float(input())
palamud = float(input())
safrid = float(input())
midi = int(input())

palamud_kg = skumria_kg * 1.6
safrid_kg = caca_kg * 1.8
midi_kg = 7.5

price = palamud * palamud_kg + \
      midi * midi_kg + \
      safrid * safrid_kg

print(format(price, '.2f'))