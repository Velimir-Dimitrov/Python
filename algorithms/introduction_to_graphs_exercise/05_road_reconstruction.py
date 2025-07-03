def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited)


nodes_count = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count)]

edges = []

for _ in range(edges_count):
    first, second = [int(x) for x in input().split(' - ')]
    graph[first].append(second)
    graph[second].append(first)
    edges.append([min(first, second), max(second, first)])

print("Important streets:")

for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)

    visited = [False] * nodes_count

    dfs(0, graph, visited)

    if not all(visited):
        print(f"{first} {second}")

    graph[first].append(second)
    graph[second].append(first)

# # Example Inputs
# 5
# 5
# 1 - 0
# 0 - 2
# 2 - 1
# 0 - 3
# 3 - 4

# 7
# 8
# 0 - 1
# 1 - 2
# 2 - 0
# 1 - 3
# 1 - 4
# 1 - 6
# 3 - 5
# 4 - 5