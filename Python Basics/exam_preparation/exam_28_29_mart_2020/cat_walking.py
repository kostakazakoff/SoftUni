min_per_walk = int(input())
walks_per_day = int(input())
eated_cal_per_day = int(input())
burned_cals_per_day = walks_per_day * min_per_walk * 5
if burned_cals_per_day >= eated_cal_per_day / 2:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burned_cals_per_day}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burned_cals_per_day}.')