minutes_to_catch = int(input())
seconds_to_catch = int(input())
lenght = float(input())
sec_per_100 = int(input())
seconds_to_catch += minutes_to_catch * 60
time = lenght / 100 * sec_per_100
delay = (lenght / 120) * 2.5
time -= delay
diff = time - seconds_to_catch
if time <= seconds_to_catch:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {time:.3f}.')
else:
    print(f'No, Marin failed! He was {diff:.3f} second slower.')