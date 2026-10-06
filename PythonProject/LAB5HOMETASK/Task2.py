
import heapq

graph = {
    'S': [('A', 2), ('B', 4), ('C', 3)],
    'A': [('D', 6)],
    'B': [('E', 2)],
    'C': [('E', 2)],
    'D': [('G', 0)],
    'E': [('F', 1)],
    'F': [('G', 0)],
    'G': []
}

def best_first(start, goal):
    pq = [(0, start)]
    visited = set()

    while pq:
        value, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        print("Visited:", node)

        if node == goal:
            print("Goal reached!")
            return

        for neighbor, priority in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (priority, neighbor))

    print("Goal not found")

best_first('S', 'G')