import tuplevector as vec

#  https://github.com/connorferster/tuplevector
# print(vec.add(P1, T1))

row_length = 0
row_count = 0

walls_coords = set()
boxes_coords = set()
robot_coords = None
move_dict = {
    '<': (-1, 0),
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1)
}

def can_move(coords, direction, char_to_move):
    next_coords = vec.add(coords, move_dict.get(direction))
    if next_coords in walls_coords:
        return (False, coords, '#')
    if next_coords in boxes_coords:
        if can_move(next_coords, direction, 'O')[0]:
            return (True, next_coords, 'O')
        else:
            return (False, next_coords, 'O')
    
    return (True, coords, char_to_move)

def move(char_to_move, coords, direction):
    global robot_coords, boxes_coords, move_dict
    next_coords = vec.add(coords, move_dict.get(direction))
    if char_to_move == '@':
        robot_coords = next_coords
    if char_to_move == 'O':
        print('O from', coords, 'to', next_coords)
        # if there is another box in front, move it first
        if next_coords in boxes_coords:
            move('O', next_coords, direction)
            print('moved boxes_coords', boxes_coords)

        boxes_coords.add(next_coords)
        # box is not in its previous position anymore
        boxes_coords.remove(coords)
        print('moved 2 boxes_coords', boxes_coords)

with open('map.txt', mode='r', encoding='utf-8') as f:
    for index_y, line in enumerate(f):
        row_count = index_y + 1
        if row_length == 0:
            row_length = len(line.strip('\n\r'))
        for index_x, char in enumerate(line):
            # find the robot starting point if we haven't found it yet
            if robot_coords is None and char == '@':
                robot_coords = (index_x, index_y)
            if char == '#':
                walls_coords.add((index_x, index_y))
            if char == 'O':
                boxes_coords.add((index_x, index_y))

with open('moves.txt', mode='r', encoding='utf-8') as f:
    for index1, moves in enumerate(f):
        moves = moves.strip()
        for index, m in enumerate(moves):
            print('index1', index1, 'index', index)
            test_move = can_move(robot_coords, m, '@')
            print(test_move)
            if test_move[0]:
                move('@', robot_coords, m)
                if test_move[2] == 'O':
                    move('O', test_move[1], m)

print('new robot_coords', robot_coords)
print('new boxes_coords', boxes_coords)
print(sum(list(map(lambda coord: 100 * coord[1] + coord[0], boxes_coords))))
            