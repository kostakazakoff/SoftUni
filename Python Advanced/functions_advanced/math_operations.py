from collections import deque


def math_operations(*args, **operations):
    def exec_operations():
        def a():
            return value + num

        def s():
            return value - num

        def d():
            if num == 0:
                return value
            return value / num

        def m():
            return value * num

        for key, value in operations.items():
            if not numbers:
                return operations
            num = numbers.popleft()
            operations[key] = eval(f'{key}()')
        return exec_operations()

    numbers = deque(args)
    exec_operations()
    output = ''
    for k, v in dict(sorted(operations.items(), key=lambda x: (-x[1], x[0]))).items():
        output += f'{k}: {v:.1f}\n'

    return output


print(math_operations(6.0, a=0, s=0, d=5, m=0))