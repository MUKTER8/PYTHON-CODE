# Depth-First Search (DFS) Algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(str(start) + " ", end="")
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

if __name__ == "__main__":
    graph = {}
    n = int(input("Total vertices: "))
    for _ in range(n):
        node = int(input("Node  :"))
        edges = input("Neighbor:")
        graph[node] = list(map(int, edges.strip().split()))
    start = int(input("\nEnter the starting vertex for DFS: "))
    dfs(graph, start)
