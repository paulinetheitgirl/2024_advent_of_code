from collections import namedtuple
from typing import NamedTuple, List
from pprint import pprint 

#  https://github.com/connorferster/tuplevector
import tuplevector as vec
from collections import deque  # Import deque for efficient queue operation

current_pos = None
obstacles = set()
total_steps = set()
row_count = 1024
grid_size = 71
#  only up, down, left, or right
unoptimized_vertex_ops = [(0, -1), (0, 1), (-1, 0), (1, 0)]

end_node = (grid_size -1, grid_size -1)
tree = {
    (0, 0): []
}
possible_paths = [[(0, 0)]]

# Modified from https://www.datacamp.com/tutorial/breadth-first-search-in-python
# Define the BFS function
def bfs(tree, start):
    global possible_paths
    visited = []  # List to keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the starting node

    while queue:  # While there are still nodes to process
        node = queue.popleft()  # Dequeue a node from the front of the queue

        if node not in visited:  # Check if the node has been visited
            visited.append(node)  # Mark the node as visited
            # print(node, end=" ")  # Output the visited node
            if node == end_node:
                break

            # Enqueue all unvisited neighbors (children) of the current node
            next_paths = []
            for neighbor in tree[node]:
                if neighbor not in visited:
                    queue.append(neighbor)  # Add unvisited neighbors to the queue
                    previous_path = next((x for x in possible_paths if x[-1] == node), None)
                    if previous_path is not None:
                        next_paths.append(previous_path + [neighbor])
            # eliminate impossible paths
            possible_paths = [p for p in possible_paths if not p[-1] == node]
            possible_paths = possible_paths + next_paths
    possible_path_lengths = sorted([len(p) - 1 for p in possible_paths])
    print(possible_path_lengths)

with open('adventofcode_18.txt', mode='r', encoding='utf-8') as f:
    for index, line in enumerate(f):
        if index >= row_count:
            break

        coords = line.strip('\n\r').split(',')
        obstacles.add((int(coords[0]), int(coords[1])))

grid_range = range(grid_size)
grid_limits = list(grid_range)
for x in grid_range:
    for y in grid_range:
        next_nodes = tree.get((x, y))
        next_nodes = [] if next_nodes is None else next_nodes
        for op in unoptimized_vertex_ops:
            current_node = (x, y)
            next_node = vec.add(current_node, op)
            if not (next_node in obstacles) and \
                next_node[0] in grid_limits and next_node[1] in grid_limits:
                next_nodes.append(next_node)
        
        tree[(x, y)] = next_nodes

possible_paths = [[(0, 0)] for i in range(len(tree.get((0, 0))))]
bfs(tree, (0, 0))