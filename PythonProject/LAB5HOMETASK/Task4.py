
import heapq

graph = {
    'S': [('A', 3), ('B', 2), ('C', 4)],
    'A': [('D', 4)],
    'B': [('E', 3)],
    'C': [('E', 2), ('F', 5)],
    'D': [('G', 5)],
    'E': [('F', 2)],
    'F': [('G', 3)],
    'G': []
}

heuristic = {
    'S': 10,
    'A': 9,
    'B': 8,
    'C': 7,
    'D': 5,
    'E': 5,
    'F': 3,
    'G': 0
}

def astar(start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        h = heuristic[node]
        print(node, "g =", g, "h =", h, "f =", f)

        if node == goal:
            print("Final Route:", path)
            print("Total Cost:", g)
            return

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

astar('S', 'G')