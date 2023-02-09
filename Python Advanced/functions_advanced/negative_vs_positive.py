def negative_positive(*args):
    numbers = list(map(int, args))
    negative = []
    positive = []
    [negative.append(x) if x < 0 else positive.append(x) for x in numbers]
    print(sum(negative))
    print(sum(positive))
    if abs(sum(negative)) > sum(positive):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


line = input().split()
negative_positive(*line)