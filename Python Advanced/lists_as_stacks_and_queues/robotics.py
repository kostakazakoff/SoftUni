from collections import deque


def count_time():
    global seconds, minutes, hours
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if hours == 24:
        hours = 0


def check_robots_availability():
    global robots
    for robot in robots:
        if robots[robot][WORKTIME] == robots[robot][PROCESSING_TIME]:
            robots[robot][WORKTIME] = 0
            robots[robot][AVAILABLE] = True


def robots_operate():
    global robots
    count_products = 0
    for robot in robots:
        if robots[robot][AVAILABLE] and count_products < 1:
            print(f"{robot} - {products.popleft()} [{hours:0>2d}:{minutes:0>2d}:{seconds:0>2d}]")
            robots[robot][AVAILABLE] = False
            count_products += 1
        if not robots[robot][AVAILABLE]:
            robots[robot][WORKTIME] += 1
    if count_products == 0:
        products.append(products.popleft())


robots_processing_times = input().split(';')
hours, minutes, seconds = list(map(int, input().split(':')))
robots = {}
products = deque()
PROCESSING_TIME = 'Processing time'
WORKTIME = "Work time"
AVAILABLE = 'Available'

for robot in robots_processing_times:
    robot, processing_time = robot.split('-')
    robots[robot] = {PROCESSING_TIME: int(processing_time), WORKTIME: 0, AVAILABLE: True}

product = input()
while product != 'End':
    products.append(product)
    product = input()

while products:
    count_time()
    check_robots_availability()
    robots_operate()

