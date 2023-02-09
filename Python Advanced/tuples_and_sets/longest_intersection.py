def set_from_range(current_range: str):
    start, end = [int(x) for x in current_range.split(',')]
    return {x for x in range(start, end + 1)}


number_of_lines = int(input())
longest_intersection = set()

for _ in range(number_of_lines):
    range1, range2 = [range for range in input().split('-')]
    intersection = set_from_range(range1) & set_from_range(range2)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

longest_intersection_output = str([x for x in longest_intersection])
print(f'Longest intersection is {longest_intersection_output} with length {len(longest_intersection)}')
