# Calculator
Create a class called Calculator that has the following static methods:
- add(*args) - sums all the arguments passed to the function and returns the result
- multiply(*args) - multiplies all the numbers and returns the result
- divide(*args) - divides all the numbers (starting from the first one) and returns the result
- subtract(*args) - subtracts all the numbers (starting from the first one) and returns the result


# Shop
Create a class called Shop. Upon initialization, it should receive a name (str), type (str), capacity (int). The store should also have an attribute called items (an empty dictionary that stores the name of an item and its quantity).
The class should have 4 methods:
- small_shop(name: str, type: str) - a new shop with a capacity of 10 should be created
- add_item(item_name:str) - adds 1 to the quantity of the given item. On success, the method should return "{item_name} added to the shop". If the addition is not possible, the following message should be returned "Not enough capacity in the shop"
- remove_item(item_name:str, amount:int) - removes the given amount from the item.
    - On success, it should return "{amount} {item_name} removed from the shop".
    - Otherwise, the method should return "Cannot remove {amount} {item_name}"
    - If the item quantity reaches 0, the item should be removed from the items' dictionary.
- __repr__() - returns a string representation in the format "{shop_name} of type {shop_type} with capacity {shop_capacity}"


# Integer
Create a class called Integer. Upon initialization, it should receive a single parameter value (int). It should have 3 additional methods:
- from_float(float_value) - creates a new instance by flooring the provided floating number.
    - If the value is not a float, return a message "value is not a float"
- from_roman(value) - creates a new instance by converting the roman number (as string) to an integer
- from_string(value) - creates a new instance by converting the string to an integer
    - if the value cannot be converted, return a message "wrong type"


# Hotel Rooms
In a folder called project create two files: hotel.py and room.py
In the room.py file, create a class called Room. Upon initialization, it should receive a number (int) and a capacity (int). It should also have an attribute called guests (0 by default) and is_taken (False by default). The class should have 2 additional methods:
- take_room(people) - if the room is not taken, and there is enough space, the guests take the room. Otherwise, the method should return "Room number {number} cannot be taken"
- free_room() - if the room is taken, free it. Otherwise, return "Room number {number} is not taken"

In the hotel.py file, create a class called Hotel. Upon initialization, it should receive a name (str). It should also have 2 more attributes: rooms (empty list of rooms) and guests (0 by default). The class should have 5 more methods:
- from_stars(stars_count: int) - creates a new instance with name "{stars_count} stars Hotel"
- add_room(room: Room) - adds the room to the list of rooms
- take_room(room_number, people) - finds the room with that number and tries to accommodate the guests in the room
- free_room(room_number) - finds the room with that number and tries to free it
- status() - returns information about the hotel in the following format:
    > "Hotel {name} has {guests} total guests
    >
    > Free rooms: {numbers of all free rooms separated by comma and space}
    >
    > Taken rooms: {numbers of all taken rooms separated by comma and space}"