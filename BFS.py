import time

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items
        # return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)

row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]
def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze[0])
    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != 0

offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}
def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path

def bfs(maze, start, goal,res):
    queue = Queue()
    queue.enqueue(start)
    predecessors = {start: None}

    while queue:
        current_cell = queue.dequeue()
        if current_cell == goal:
            res[current_cell[0]][current_cell[1]] = 1
            return get_path(predecessors, start, goal)

        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                queue.enqueue(neighbour)
                predecessors[neighbour] = current_cell
                res[current_cell[0]][current_cell[1]] = 1

        # res[current_cell[0]][current_cell[1]] = 0

    return None

if __name__ == "__main__":
    # Test 1
    start = time.time()
    maze = [[1,1,0],
            [1,1,0],
            [1,1,1]
            ]
    res = [[0 for j in range(3)]for i in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    if bfs(maze, start_pos, goal_pos,res):
        for i in res:
            print(i)
        print()
    end = time.time()
    print(end-start)

    # assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]