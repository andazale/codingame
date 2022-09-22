# https://www.codingame.com/ide/puzzle/blunder-episode-1

import sys
import numpy as np

directions = {
    (1, 0) : 'SOUTH',
    (0, 1) : 'EAST',
    (-1, 0) : 'NORTH',
    (0, -1) : 'WEST'
}

south = (1, 0)
east = (0, 1)
north = (-1, 0)
west = (0, -1)

l, c = [int(i) for i in input().split()] # number of rows and columns
rows = np.array([list(input()) for i in range(l)], dtype=object) # the map

print(rows, file=sys.stderr, flush=True)

starting_point = np.where(rows == '@')
print("Very starting point is: ", starting_point, file=sys.stderr, flush=True)

current_point = (starting_point[0][0], starting_point[1][0])
current_direction = south
inverted = False
breaker_mode = False
moves = 0
result = []

def check_next_point(direction):
    return rows[current_point[0] + direction[0]][current_point[1] + direction[1]]

def try_step(current, breaker, invert):
    if check_next_point(current) in ['X', '#'] and not breaker or check_next_point(current) == '#':
        if not invert:
            for i in [south, east, north, west]:  
                if check_next_point(i) not in ['X', '#']:
                    return i
        else:
            for i in [west, north, east, south]:
                if check_next_point(i) not in ['X', '#']:
                    return i
    elif check_next_point(current) in ['X'] and breaker: 
        rows[current_point[0] + current[0]][current_point[1] + current[1]] = ' '
        return current
    return current

def change_point(direction):
    return (current_point[0] + direction[0], current_point[1] + direction[1])

def handle_step(direction, breaker, invert):
    next_dir = try_step(direction, breaker, invert)
    next_point = change_point(next_dir)
    return next_dir, next_point

def handle_modifier(modifier, breaker):
    next_dir = modifier
    if check_next_point(next_dir) in ['X'] and breaker: 
        rows[current_point[0] + next_dir[0]][current_point[1] + next_dir[1]] = ' '
    next_point = change_point(modifier)
    return next_dir, next_point

def handle_breaker(breaker, invert, direction):
    if breaker: breaker = False
    else: breaker = True
    next_dir, next_point = handle_step(direction, breaker, invert)
    return breaker, next_dir, next_point

def handle_inverter(invert, direction, breaker):
    if invert: invert = False
    else: invert = True
    next_dir, next_point = handle_step(direction, breaker, invert)
    return invert, next_dir, next_point

def handle_teleporter(cur_point):
    other_teleporter = np.argwhere(rows == 'T')
    other_teleporter = tuple(np.delete(other_teleporter, np.where((other_teleporter == cur_point).all(1))[0], 0)[0])
    return other_teleporter

while rows[current_point[0]][current_point[1]] != '$':
    character = rows[current_point[0]][current_point[1]]
    if character in [' ', '@']:
        current_direction, current_point = handle_step(current_direction, breaker_mode, inverted)
    elif character == 'E':
        current_direction, current_point = handle_modifier(east, breaker_mode)
    elif character == 'S':
        current_direction, current_point = handle_modifier(south, breaker_mode)
    elif character == 'N':
        current_direction, current_point = handle_modifier(north, breaker_mode)
    elif character == 'W':
        current_direction, current_point = handle_modifier(west, breaker_mode)
    elif character == 'B':
        breaker_mode, current_direction, current_point = handle_breaker(breaker_mode, inverted, current_direction)
    elif character == 'I':
        inverted, current_direction, current_point = handle_inverter(inverted, current_direction, breaker_mode)
    elif character == 'T':
        current_point = handle_teleporter(current_point)
        current_direction, current_point = handle_step(current_direction, breaker_mode, inverted)
    moves += 1
    result.append(directions[current_direction])
    if moves > 200:
        print('LOOP')
        sys.exit()

print(*result, sep='\n')
