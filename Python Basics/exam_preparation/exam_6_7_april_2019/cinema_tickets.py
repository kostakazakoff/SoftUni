name_of_the_movie = input()
they_are_no_tickets = False
there_is_no_more_place = False
student_ticket_per_day = 0
standard_ticket_per_day = 0
kid_ticket_per_day = 0
all_tickets_per_day = 0
percent_of_capacity = 0
all_student_tickets = 0
all_standard_tickets = 0
all_kid_tickets = 0
all_tickets = 0
#movie loop=================================================================================
while name_of_the_movie != 'Finish':
    capacity = int(input())
    pass
    ticket_type = input()
    #tickets loop================================================
    while ticket_type != 'End':
        if ticket_type == 'student':
            student_ticket_per_day += 1
        elif ticket_type == 'standard':
            standard_ticket_per_day += 1
        elif ticket_type == 'kid':
            kid_ticket_per_day += 1
        all_tickets_per_day += 1
        if all_tickets_per_day == capacity:
            break
        else:
            ticket_type = input()
        #end of ticket loop======================================
    all_student_tickets += student_ticket_per_day
    all_standard_tickets += standard_ticket_per_day
    all_kid_tickets += kid_ticket_per_day
    all_tickets += all_tickets_per_day
    percent_of_capacity = all_tickets_per_day * 100 / capacity
    print(f'{name_of_the_movie} - {percent_of_capacity:.2f}% full.')
    student_ticket_per_day = 0
    standard_ticket_per_day = 0
    kid_ticket_per_day = 0
    all_tickets_per_day = 0
    name_of_the_movie = input()
    #end of movie loop==========================================================================
all_student_tickets *= 100/all_tickets
all_standard_tickets *= 100/all_tickets
all_kid_tickets *= 100/all_tickets
print(f'Total tickets: {all_tickets}')
print(f'{all_student_tickets:.2f}% student tickets.')
print(f'{all_standard_tickets:.2f}% standard tickets.')
print(f'{all_kid_tickets:.2f}% kids tickets.')