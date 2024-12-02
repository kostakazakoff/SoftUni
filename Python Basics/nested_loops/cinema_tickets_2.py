name_of_the_movie = input()
student_tickets_counter = 0
standard_tickets_counter = 0
kids_tickets_counter = 0
total_tickets = 0
while name_of_the_movie != 'Finish':
    total_places = int(input())
    free_places = total_places
    tickets_for_the_movie = 0
    while free_places > 0:
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
        free_places -= 1
        total_tickets += 1
    percent_of_hall_capacity = tickets_for_the_movie / total_places * 100
    print(f'{name_of_the_movie} - {percent_of_hall_capacity:.2f}% full.')
    name_of_the_movie = input()
percent_student_tickets = student_tickets_counter / total_tickets * 100
percent_standard_tickets = standard_tickets_counter / total_tickets * 100
percent_kids_tickets = kids_tickets_counter / total_tickets * 100
print(f'Total tickets: {total_tickets}')
print(f'{percent_student_tickets:.2f}% student tickets.')
print(f'{percent_standard_tickets:.2f}% standard tickets.')
print(f'{percent_kids_tickets:.2f}% kids tickets.')

