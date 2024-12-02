grade = float(input())


def result(number):
    if 2 <= number < 3:
        return 'Fail'
    elif number < 3.5:
        return 'Poor'
    elif number < 4.5:
        return 'Good'
    elif number < 5.5:
        return 'Very Good'
    elif number <= 6:
        return 'Excellent'


print(result(grade))
