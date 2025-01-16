import tuplevector as vec

#  https://github.com/connorferster/tuplevector
# print(vec.add(P1, T1))

current_pos = None
obstacles = []
move_direction = (0, -1)
total_steps = set()
row_length = 0
row_count = 0
#  only up, down, left, or right
unoptimized_vertex_ops = [(0, -1), (0, 1), (-1, 0), (1, 0)]
vertices_by_number = [set() for i in range(10)] # numbers 0-9 have their own sets

with open('adventofcode_10.txt', mode='r', encoding='utf-8') as f:
    # save (x,y) tuple for every number in the file
    for index_y, line in enumerate(f):
        row_count = index_y + 1
        line = line.strip('\n\r')
        if row_length == 0:
            row_length = len(line)
        for index_x, char in enumerate(line):
            vertices_by_number[int(char)].add((index_x, index_y))

current_height = 9
possible_paths = []
for s in vertices_by_number[9]:
        possible_paths.append([s])

while current_height > 0:
    previous_height = current_height - 1
    next_paths = []

    for p in possible_paths:
        for op in unoptimized_vertex_ops:
            prev_vertex = vec.add(p[-1], op)
            if prev_vertex in vertices_by_number[previous_height]:
                next_paths.append(p + [prev_vertex])

    # eliminate impossible paths
    possible_paths = next_paths
    current_height -= 1

print("possible_paths", len(possible_paths))
