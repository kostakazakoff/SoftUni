project_time_in_hours = int(input())
all_days = int(input())
employee = int(input())

days = all_days * 0.9
hours = days * 8
extra_time = all_days * employee * 2
all_time_for_work = int(hours + extra_time)
difference = int(abs(all_time_for_work - project_time_in_hours))

if project_time_in_hours <= all_time_for_work:
    print(f'Yes!{difference} hours left.')
else:
    print(f'Not enough time!{difference} hours needed.')