def electron_distribution(number_of_electrons):
    shell = 0
    list_of_shells = []
    while number_of_electrons > 0:
        shell += 1
        # Defining the maximum electrons in a shell by given formula:
        max_electrons_in_shell = 2 * shell ** 2
        # Adding the electrons to the shell (if less than maximum number - adding the rest of it):
        list_of_shells += [max_electrons_in_shell] if max_electrons_in_shell <= number_of_electrons else [number_of_electrons]
        number_of_electrons -= max_electrons_in_shell
    return list_of_shells


electrons = int(input())
print(electron_distribution(electrons))
