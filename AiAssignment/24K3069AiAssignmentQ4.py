maze = [
    ['S', 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 'G']
]

rows = len(maze)
cols = len(maze[0])

start = (0, 0)
goal = (4, 5)

# Down, Right, Up, Left
directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]


def get_neighbors(position):
    row, col = position
    neighbors = []

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < rows and 0 <= new_col < cols:
            if maze[new_row][new_col] != 1:
                neighbors.append((new_row, new_col))

    return neighbors


def show_path(path):
    if path is None:
        return "No path"

    return " -> ".join(str(x) for x in path)


def bfs():
    frontier = [(start, [start])]
    visited = {start}
    expanded = 0

    while frontier:
        node, path = frontier.pop(0)

        if node == goal:
            return path, expanded

        expanded += 1

        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                frontier.append((neighbor, path + [neighbor]))

    return None, expanded


def dls(limit):
    frontier = [(start, [start], 0)]
    expanded = 0

    while frontier:
        node, path, depth = frontier.pop()

        if node == goal:
            return path, expanded

        if depth == limit:
            continue

        expanded += 1

        neighbors = get_neighbors(node)

        for neighbor in reversed(neighbors):
            if neighbor not in path:
                frontier.append(
                    (neighbor, path + [neighbor], depth + 1)
                )

    return None, expanded


def ids():
    total_expanded = 0
    limit = 0

    while True:
        path, expanded = dls(limit)

        print("Depth Limit:", limit)
        print("Goal Found:", "Yes" if path else "No")
        print("Path Length:", len(path) - 1 if path else "-")
        print("Nodes Expanded:", expanded)
        print()

        total_expanded += expanded

        if path:
            return path, total_expanded

        limit += 1


print("========== BFS ==========")

path, expanded = bfs()

print("Path:", show_path(path))
print("Path Length:", len(path) - 1 if path else "-")
print("Nodes Expanded:", expanded)
print("Goal Found:", "Yes" if path else "No")


print("\n========== DLS ==========")

for limit in [2, 4, 6, 9]:
    path, expanded = dls(limit)

    print("Depth Limit:", limit)
    print("Path:", show_path(path))
    print("Path Length:", len(path) - 1 if path else "-")
    print("Nodes Expanded:", expanded)
    print("Goal Found:", "Yes" if path else "No")
    print()


print("========== IDS ==========")

path, total_expanded = ids()

print("Final IDS Path:", show_path(path))
print("Final Path Length:", len(path) - 1)
print("Total Nodes Expanded:", total_expanded)