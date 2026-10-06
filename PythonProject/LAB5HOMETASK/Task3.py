
import heapq

graph = {
    'S': [('B', 2), ('C', 4)],
    'B': [('G', 2)],
    'C': [('D', 1)],
    'D': [('G', 1)],
    'G': []
}

heuristic = {
    'S': 3,
    'B': 2,
    'C': 1,
    'D': 1,
    'G': 0
}

def greedy(start, goal):
    pq = [(heuristic[start], start, [start])]
    visited = set()

    while pq:
        h, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        print("Visited:", node, "h =", h)

        if node == goal:
            print("Route:", path)
            return

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (heuristic[neighbor], neighbor,
                     path + [neighbor])
                )

    print("Goal not found")

greedy('S', 'G')