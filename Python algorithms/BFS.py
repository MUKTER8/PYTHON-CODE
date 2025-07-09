# Breadth-First Search (BFS) Algorithm
import collections


def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)  # Mark the root as visited

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


if __name__ == "__main__":
    graph = {}
    n = int(input("Total vertices: "))
    for _ in range(n):
        node = int(input("Node  :"))
        edges = input("Neighbor:")
        graph[node] = list(map(int, edges.strip().split()))
    start = int(input("\nEnter the starting vertex for BFS: "))
    bfs(graph, start)
