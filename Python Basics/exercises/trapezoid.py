b1 = float(input())
b2 = float(input())
h = float(input())

face = (b1 +b2) * h / 2
face_2 = format(face, '.2f') #give 2 digits after the point
face_3 = format(face, '.7g') #give 7 significant digits

print(face_2)
print(face_3)
print(face)
