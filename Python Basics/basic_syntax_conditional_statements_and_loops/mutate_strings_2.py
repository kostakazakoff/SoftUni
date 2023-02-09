first_string = input()
second_string = input()
current = first_string

for i in range(len(first_string)):
    left = second_string[:i + 1]
    right = first_string[i + 1:]
    mutated_string = left + right
    if mutated_string != current:
        print(mutated_string)
    current = mutated_string
