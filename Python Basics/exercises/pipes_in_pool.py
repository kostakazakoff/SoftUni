v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

pipe1 = p1 * h
pipe2 = p2 * h
volume = pipe1 + pipe2

pipe1_percent = pipe1 * 100 / volume
pipe2_percent = pipe2 * 100 / volume


percent = volume * 100 / v

if volume <= v:
    print(f"The pool is {percent}% full. Pipe 1: {pipe1_percent}%. Pipe 2: {pipe2_percent}%.")
else:
    difference = volume - v
    print(f"For {h} hours the pool overflows with {difference} liters.")