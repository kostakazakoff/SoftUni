tournament_duration = int(input())
award = 0
wins_number_for_a_day = 0
lose_number_for_a_day = 0
days_of_tournament = 0
victory_days = 0
profit = 0
total_profit = 0
you_are_the_tournament_winner = False
#========================================================================================================
for days_of_tournament in range(1, tournament_duration + 1):
    command = input()
    #==============================================================================
    while command != 'Finish':
        sport = command
        result = input()
        if result == 'win':
            award += 20
            wins_number_for_a_day += 1
        elif result == 'lose':
            lose_number_for_a_day += 1
        command = input()
    #==============================================================================
    profit += award
    if wins_number_for_a_day > lose_number_for_a_day:
        profit *= 1.1
        victory_days += 1
    total_profit += profit
    award = 0
    profit = 0
    wins_number_for_a_day = 0
    lose_number_for_a_day = 0
#======================================================================================================
if victory_days > tournament_duration / 2:
    total_profit *= 1.2
    you_are_the_tournament_winner = True
if you_are_the_tournament_winner:
    print(f'You won the tournament! Total raised money: {total_profit:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_profit:.2f}')