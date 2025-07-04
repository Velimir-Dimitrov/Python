def dfs(node, graph, visited, component):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.append(node)



number_of_nodes = int(input())
graph = []
visited = [False] * number_of_nodes

for i in range(number_of_nodes):
    node_input = [int(num) for num in input().split()]
    graph.append(node_input)


for node in range(number_of_nodes):
    if visited[node]:
        continue
    component = []
    dfs(node, graph, visited, component)
    print(f"Connected component: {' '.join(str(num) for num in component)}")

# # Example input
# 9
# 3 6
# 3 4 5 6
# 8
# 0 1 5
# 1 6
# 1 3
# 0 1 4
#
# 2
