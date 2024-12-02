symbols = tuple(s for s in input())
set_of_symbols = set(symbols)
[print(f'{symbol}: {symbols.count(symbol)} time/s') for symbol in sorted(set_of_symbols)]