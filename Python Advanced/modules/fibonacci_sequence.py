from utils.fibonacci_helper import Fibonacci_sequence


f = Fibonacci_sequence()
line = input()
num_idx = None

while line != 'Stop':
    action, n = line.split()[0], int(line.split()[-1])
    
    if action == 'Create':
        f.create(n)
        print(f.sequence)

    else:
        num_idx = f.sequence.index(n) if n in f.sequence else None

        if num_idx:
            print(f"The number - {n} is at index {num_idx}")
        else:
            print(f"The number {n} is not in the sequence")

    line = input()