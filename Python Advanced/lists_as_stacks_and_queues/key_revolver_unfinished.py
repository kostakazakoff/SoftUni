from collections import deque


def load_bullets_to_stack():
    global bullets_barrel_stack, bullets
    [bullets_barrel_stack.append(int(bullet)) for bullet in bullets.split()]


def load_locks_to_queue():
    global locks_queue, locks
    [locks_queue.append(int(lock)) for lock in locks.split()]


def load_gun():
    global bullets_barrel_stack, gun_stack, first_load
    if START_BULLETS_QUANTITY != len(bullets_barrel_stack):
        first_load = False
    for _ in range(gun_barrel_size):
        if bullets_barrel_stack:
            gun_stack.append(bullets_barrel_stack.pop())
    if not first_load and gun_stack:
        print('Reloading!')


def shoot_locks():
    global total_bullets_fired, locks_queue, gun_stack
    for _ in range(len(gun_stack)):
        if locks_queue:
            fired_bullet_size = gun_stack.popleft()
            total_bullets_fired += 1
            if fired_bullet_size <= locks_queue[0]:
                locks_queue.popleft()
                print('Bang!')
            else:
                print('Ping!')


bullet_price = int(input())
gun_barrel_size = int(input())
bullets = input()
locks = input()
intelligence = int(input())

first_load = True
bullets_barrel_stack = []
locks_queue = deque()
gun_stack = deque()
locks_destroyed = False
total_bullets_fired = 0

load_bullets_to_stack()
load_locks_to_queue()

START_BULLETS_QUANTITY = len(bullets_barrel_stack)

load_gun()
while True:
    shoot_locks()
    load_gun()
    if not locks_queue or not gun_stack:
        break


if len(locks_queue) == 0:
    bullets_left = len(bullets_barrel_stack) + len(gun_stack)
    expense = (START_BULLETS_QUANTITY - bullets_left) * bullet_price
    print(f"{bullets_left} bullets left. Earned ${intelligence - expense}")
else:
    print(f"Couldn't get through. Locks left: {len(locks_queue)}")