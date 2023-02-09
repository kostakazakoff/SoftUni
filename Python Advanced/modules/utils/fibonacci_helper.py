class Fibonacci_sequence:
    def __init__(fibonacci):
        fibonacci.sequence = [0, 1]

    def create(fibonacci, count):
        fibonacci.sequence = [0, 1]
        while count:
            if count > 2: fibonacci.sequence.append(sum(fibonacci.sequence[-2:]))
            count -= 1


# def fib(count: int):
#     global fib_sequence
#     if count > 2: fib_sequence.append(sum(fib_sequence[-2:]))
#     if count == 0: return
#     fib(count - 1)


# fib_sequence = [0, 1]