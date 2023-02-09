fat_percent = int(input())
protein_percent = int(input())
carbohydrates_percent = int(input())
cal_total = int(input())
water_percent = int(input())
fat = cal_total * fat_percent / 100 / 9
protein = cal_total * protein_percent / 100 / 4
carbohydrates = cal_total * carbohydrates_percent / 100 / 4
food_content = fat + protein + carbohydrates
cal_per_g = cal_total / food_content
water_per_g = cal_per_g * water_percent / 100
cal_per_g = cal_per_g - water_per_g
print(f'{cal_per_g:.4f}')