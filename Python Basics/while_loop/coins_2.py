def change(x):
    x = float(input())
    x = int(100 * sum)
    result = 0
    coin_value = (200, 100, 50, 20, 10, 5, 2, 1)
    for coins in coin_value:
        result += x // coins
        x = x % coins

money = float(input())
result = change(money)
print(result)