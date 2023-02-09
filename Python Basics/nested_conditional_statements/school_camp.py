season = input()
group_type = input()
students_number = int(input())
days = int(input())
sport = ''
price = 0
if season == 'Winter':
    price = 9.6
    if group_type == 'mixed':
        sport = 'Ski'
        price = 10
    elif group_type == 'girls':
        sport = 'Gymnastics'
    elif group_type == 'boys':
        sport = 'Judo'
elif season == 'Spring':
    price = 7.2
    if group_type == 'mixed':
        sport = 'Cycling'
        price = 9.5
    elif group_type == 'girls':
        sport = 'Athletics'
    elif group_type == 'boys':
        sport = 'Tennis'
elif season == 'Summer':
    price = 15
    if group_type == 'mixed':
        sport = 'Swimming'
        price = 20
    elif group_type == 'girls':
        sport = 'Volleyball'
    elif group_type == 'boys':
        sport = 'Football'
price *= students_number * days
if students_number >= 50:
    price *= 0.5
elif students_number >= 20:
    price -= price * 0.15
elif students_number >= 10:
    price -= price * 0.05

print(f'{sport} {price:.2f} lv.')