import math

record_in_seconds = float(input())
distance = float(input())
seconds_per_m = float(input())

clean_time = (distance * seconds_per_m)
distance_15_meters = math.floor(distance / 15)
late = (distance_15_meters * 12.5)
total_time = (clean_time + late)
sec_to_record = abs(record_in_seconds - total_time)

if total_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {sec_to_record:.2f} seconds slower.")