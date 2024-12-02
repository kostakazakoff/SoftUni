batches = int(input())
total_boxes = 0

for batch in range(batches):
    flour = int(input())
    sugar = int(input())
    cocoa = int(input())

    cookies_per_bake, boxes_per_bake = 0, 0
    cups = flour // 140
    small_spoons = cocoa // 10
    big_spoons = sugar // 20

    ingredients = [cups, small_spoons, big_spoons]
    ingredients.sort()
    min = ingredients[0]
    if min < 1:
        print('Ingredients are not enough for a box of cookies.')
    else:
        cookies_per_bake = 170 * min // 25
        boxes_per_bake = cookies_per_bake // 5
        total_boxes += boxes_per_bake
        print(f'Boxes of cookies: {boxes_per_bake}')

print(f'Total boxes: {total_boxes}')