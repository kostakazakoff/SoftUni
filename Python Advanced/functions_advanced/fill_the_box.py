def fill_the_box(*args):
    def get_boxes(i=3):
        if args[i] == "Finish":
            return boxes_to_use
        boxes_to_use.append(args[i])
        return get_boxes(i + 1)

    boxes_to_use = []
    box_volume = args[0] * args[1] * args[2]
    boxes_volume = sum(get_boxes())
    difference = box_volume - boxes_volume
    if difference > 0:
        return f"There is free space in the box. You could put {difference} more cubes."
    return f"No more free space! You have {abs(difference)} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
