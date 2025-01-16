from collections import namedtuple
from typing import NamedTuple, List
from pprint import pprint 
import tuplevector as vec

#  https://github.com/connorferster/tuplevector
# Point = NamedTuple("Point", [("x", int),
#                              ("y", int)])
                             
# P1 = Point(6, 7)
# T1 = (1, 2)
# print(vec.add(P1, T1))

current_pos = None
obstacles = []
move_direction = (0, -1)
total_steps = set()
row_length = 0
row_count = 0
next_move_dict = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1)
}

def move(current_pos):
    global total_steps, move_direction, row_length, row_count
    next_pos = vec.add(current_pos, move_direction)
    print(current_pos, move_direction, next_pos)
    while not(next_pos in obstacles):
        total_steps.add(current_pos)
        current_pos = tuple(next_pos)
        next_pos = vec.add(current_pos, move_direction)
        # reached an edge
        if (next_pos[0] < 0) or \
            (next_pos[0] > row_length - 1) or \
            (next_pos[1] < 0) or \
            (next_pos[1] > row_count - 1):
            break;
    # change direction
    move_direction = tuple(next_move_dict.get(move_direction))
    # reached an edge
    if (next_pos[0] < 0) or \
        (next_pos[0] > row_length - 1) or \
        (next_pos[1] < 0) or \
        (next_pos[1] > row_count - 1):
        total_steps.add(current_pos)
        return
    move(current_pos)

with open('adventofcode_6.txt', mode='r', encoding='utf-8') as f:
    for index_y, line in enumerate(f):
        row_count = index_y + 1
        if row_length == 0:
            row_length = len(line.strip('\n\r'))
        for index_x, char in enumerate(line):
            # find the starting point if we haven't found it yet
            if current_pos is None and char == '^':
                current_pos = (index_x, index_y)
            if char == '#':
                obstacles.append((index_x, index_y))

print(current_pos, ' ', row_count, ' ', row_length)
pprint(obstacles)
move(current_pos)
print('steps', len(total_steps))

            