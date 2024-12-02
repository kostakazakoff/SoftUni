x = float(input())
y = float(input())
h = float(input())

door_face = 1.2 * 2
windows_face = (1.5 ** 2) * 2

walls_square = 2 * (x ** 2)
walls_rectangle = 2 * x * y
walls = walls_square + walls_rectangle - door_face - windows_face

roof_triangles = x * h
roof_rectangles = 2 * x * y
roof = roof_triangles + roof_rectangles

green_paint_l_for_sqm = 3.4
red_paint_l_for_sqm = 4.3

green = walls / green_paint_l_for_sqm
red = roof / red_paint_l_for_sqm

print(format(green, '.2f'))
print(format(red, '.2f'))