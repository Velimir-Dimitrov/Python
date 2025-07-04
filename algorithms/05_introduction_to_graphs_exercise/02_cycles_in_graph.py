def dfs(node, visited, graph, cycles):
    if node in cycles:
        raise Exception
    if node in visited:
        return

    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, visited, graph, cycles)

    cycles.remove(node)


graph = {}
while True:
    line = input()

    if line == 'End':
        break

    source, destination = line.split('-')
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(destination)

try:
    visited = set()
    for node in graph:
        dfs(node, visited, graph, set())
    print("Acyclic: Yes")
except Exception:
    print("Acyclic: No")


# # Example inputs
# A-F
# F-D
# D-A
# End

# E-Q
# Q-P
# P-B
# End