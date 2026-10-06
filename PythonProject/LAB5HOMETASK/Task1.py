
from collections import deque

maze = [
    "S...#",
    ".#..G",
    ".#.#.",
    "...G.",
    "G...."
]

start = (0, 0)
goals = {(1, 4), (3, 3), (4, 0)}

queue = deque([(start, [start], frozenset())])
visited = set()

while queue:
    pos, path, found = queue.popleft()

    if pos in goals:
        found = found | {pos}

    if found == goals:
        print("Path:", path)
        print("Steps:", len(path) - 1)
        break

    state = (pos, found)
    if state in visited:
        continue
    visited.add(state)

    r, c = pos

    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
            if maze[nr][nc] != '#':
                queue.append(((nr, nc), path + [(nr, nc)], found))
else:
    print("No path found")