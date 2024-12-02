def available_chairs_in_room(room_and_people: str):
    # Splitting the available and needed chairs to list:
    engagement = room_and_people.split()
    available = len(engagement[0])
    # If they are no visitors in this room, return the number of chairs:
    if len(engagement) == 1:
        return available
    # If they are visitors, return the difference:
    return available - int(engagement[1])


def capacity(number_of_rooms: int):
    total_chairs = 0
    # Creating a list of messages for not enough chairs in the current room:
    not_enough_message = []
    # Walking around the rooms and check for the capacity (room 1 to room n):
    for room in range(1, number_of_rooms + 1):
        room_input = input()
        # Taking the result from the available_chairs_in_room() function:
        chairs_difference = available_chairs_in_room(room_input)
        # Counting the total chairs:
        total_chairs += chairs_difference
        # Adding the room message to the message list (if they are not enough chairs):
        if chairs_difference < 0:
            not_enough_message.append(f'{abs(chairs_difference)} more chairs needed in room {room}')
    # Defining the not_enough bool value and returning the function results:
    not_enough = total_chairs < 0
    return abs(total_chairs), '\n'.join(not_enough_message), not_enough


rooms_count = int(input())

# Getting up the results from the function:
free_chairs, message, not_enough_chairs = capacity(rooms_count)
# If they are some chair needs in any of the rooms:
if not_enough_chairs:
    print(message)
# Everything is O.K. The chairs are enough:
else:
    print(f'Game On, {free_chairs} free chairs left')
