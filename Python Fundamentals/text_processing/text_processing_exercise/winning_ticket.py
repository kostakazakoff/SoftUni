def check_ticket(ticket: str):
    wining_simbols = ['@', '#', '$', '^']
    left = ticket[:10]
    right = ticket[10:]
    ticket_length = len(left) + len(right)
    if ticket_length != 20:
        return 'invalid ticket'
    for symbol in wining_simbols:
        for i in range(10, 5, -1):
            win_symbols = i * symbol
            if win_symbols in left and win_symbols in right:
                if len(win_symbols) == 10:
                    return f'ticket "{ticket}" - 10{symbol} Jackpot!'
                return f'ticket "{ticket}" - {i}{symbol}'
    return f'ticket "{ticket}" - no match'


entered_tickets = [x.strip() for x in input().split(', ')]
for entered_ticket in entered_tickets:
    print(check_ticket(entered_ticket))
