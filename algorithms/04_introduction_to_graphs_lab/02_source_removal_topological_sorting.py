def get_predecessors_count(graph):
    result = {}

    for node, children in graph.items():
        if node not in result:
            result[node] = 0

        for child in children:
            if child not in result:
                result[child] = 0
            result[child] += 1

    return result

def find_node_without_predecessors(predecessors_count):
    for node, children in predecessors_count.items():
        if children == 0:
            return node
    return None



def topological_sort(graph, predecessors_count):
    result = []

    while predecessors_count:
        node_to_remove = find_node_without_predecessors(predecessors_count)
        if node_to_remove is None:
            result = False
            break

        for child in graph[node_to_remove]:
            predecessors_count[child] -= 1

        result.append(node_to_remove)
        predecessors_count.pop(node_to_remove)

    return result



nodes = int(input())
graph = {}


for line in range(nodes):
    input_line = input().split(' ->')
    node = input_line[0]
    children = input_line[1].strip().split(', ') if input_line[1] != '' else []
    graph[node] = children



predecessors_count = get_predecessors_count(graph)
sorted_nodes = topological_sort(graph, predecessors_count)

if sorted_nodes:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")
else:
    print('Invalid topological sorting')


# # Example input

# 6
# A -> B, C
# B -> D, E
# C -> F
# D -> C, F
# E -> D
# F ->


# 5
# IDEs -> variables, loops
# variables -> conditionals, loops, bits
# conditionals -> loops
# loops -> bits
# bits ->


# 2
# A -> B
# B -> A

