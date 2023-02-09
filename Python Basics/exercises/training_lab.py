w = float(input())
h = float(input())
h -= 1 #-1 m za koridora
work_w = 1.2
work_h = 0.7

in_w = w // work_w
in_h = h // work_h
all = int(in_h * in_w - 3)

#print(f'{w}, {h}')
print(all)