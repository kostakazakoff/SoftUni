easter_breads = int(input())
eggs = int(input())
cookies = int(input())
eggs_paint_price = eggs * 12 * 0.15
price = easter_breads * 3.2 + eggs * 4.35 + cookies * 5.4 + eggs_paint_price
print(f'{price:.2f}')