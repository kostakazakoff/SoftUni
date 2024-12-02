def loading_bar(percent):
    x = percent // 10
    load_level = f'[{"%" * x}{"." * (10 - x)}]'
    if percent == 100:
        return f'100% Complete!\n{load_level}'
    return f'{percent}% {load_level}\nStill loading...'


bar_value = int(input())
print(loading_bar(bar_value))
