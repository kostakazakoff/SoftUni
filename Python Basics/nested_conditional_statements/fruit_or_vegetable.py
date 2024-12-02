product = input()

fruit = 'banana, apple, kiwi, cherry, lemon, grapes'
vegetable = 'tomato, cucumber, pepper, carrot'

if product in fruit:
    print('fruit')
elif product in vegetable:
    print('vegetable')
else:
    print('unknown')