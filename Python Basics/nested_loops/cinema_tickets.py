name_of_the_movie = input()
total_students_tickets = 0
total_standard_tickets = 0
total_kids_tickets = 0
total_tickets = 0
percent_of_hall_capacity = 0

while name_of_the_movie != 'Finish':

    free_places = int(input())
    student_tickets_counter = 0
    standard_tickets_counter = 0
    kids_tickets_counter = 0
    tickets_for_the_movie = 0

    while tickets_for_the_movie < free_places:
        type_of_ticket = input()
        if type_of_ticket == 'End':
            break
        elif type_of_ticket == 'student':
            student_tickets_counter += 1
        elif type_of_ticket == 'standard':
            standard_tickets_counter += 1
        elif type_of_ticket == 'kid':
            kids_tickets_counter += 1
        tickets_for_the_movie += 1

    total_students_tickets += student_tickets_counter
    total_standard_tickets += standard_tickets_counter
    total_kids_tickets += kids_tickets_counter
    total_tickets += tickets_for_the_movie
    percent_of_hall_capacity = tickets_for_the_movie / free_places * 100
    print(f'{name_of_the_movie} - {percent_of_hall_capacity:.2f}% full.')

    name_of_the_movie = input()

print(f'Total tickets: {total_tickets}')
print(f'{(total_students_tickets / total_tickets * 100):.2f}% student tickets.')
print(f'{(total_standard_tickets / total_tickets * 100):.2f}% standard tickets.')
print(f'{(total_kids_tickets / total_tickets * 100):.2f}% kids tickets.')

