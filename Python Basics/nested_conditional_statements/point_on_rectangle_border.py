x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

border_y = (x == x1 or x == x2) and (y >= y1 or y <= y2)

border_x = (y == y1 or y == y2) and (x >= x1 or x <= x2)

if border_x or border_y:
    print('Border')
else:
    print('Inside / Outside')