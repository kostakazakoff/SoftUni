def free_places(current, full):
    return [full[x] - current[x] for x in range(len(full))], sum(full) - sum(current)


people = int(input())
lift = list(map(int, input().split()))
full_lift = len(lift) * [4]
differences_in_wagons, free_places_in_lift = free_places(lift, full_lift)

if people - free_places_in_lift > 0:
    print(f"There isn't enough space! {people - free_places_in_lift} "
          f"people in a queue!\n{' '.join([str(x) for x in full_lift])}")
elif people - free_places_in_lift == 0:
    print(' '.join([str(x) for x in full_lift]))
else:
    for i, value in enumerate(differences_in_wagons):
        for _ in range(value):
            lift[i] += 1
            people -= 1
            if people == 0:
                print(f"The lift has empty spots!\n{' '.join([str(x) for x in lift])}")
                exit(2)
