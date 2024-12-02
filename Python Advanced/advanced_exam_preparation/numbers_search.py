def numbers_searching(*args):
    sequence = set(range(min(args), max(args)))
    missing_number = list(set(sequence) - set(args))[0]
    duplicates = sorted(list(set([x for x in args if args.count(x) > 1])))
    return [missing_number, duplicates]

#Test:
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))