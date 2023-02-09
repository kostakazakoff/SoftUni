budget = float(input())
number_of_series = int(input())

for i in range(number_of_series):
    series_name = input()
    series_price = float(input())
    if series_name == 'Thrones':
        series_price *= 0.5
    elif series_name == 'Lucifer':
        series_price *= 0.6
    elif series_name == 'Protector':
        series_price *= 0.7
    elif series_name == 'TotalDrama':
        series_price *= 0.8
    elif series_name == 'Area':
        series_price *= 0.9
    budget -= series_price

if budget>= 0:
    print(f'You bought all the series and left with {budget:.2f} lv.')
else:
    print(f'You need {abs(budget):.2f} lv. more to buy the series!')