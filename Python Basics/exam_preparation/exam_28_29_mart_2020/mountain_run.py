record_time = float(input())
distance = float(input())
sec_for_1_meter = float(input())

clear_time = distance * sec_for_1_meter
delay = (distance // 50) * 30
total_time = clear_time + delay
diff = total_time - record_time
if total_time < record_time:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    print(f'No! He was {diff:.2f} seconds slower.')