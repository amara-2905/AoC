from collections import defaultdict
from functools import lru_cache

graph = defaultdict(list)

with open("input.txt") as input_file:
    for line in input_file:
        source_node, destination_part = line.split(":")
        graph[source_node.strip()] += destination_part.split()

all_nodes = sorted({*graph, *sum(graph.values(), [])})
node_index = {node: index for index, node in enumerate(all_nodes)}
adjacency_matrix = [[int(destination in graph[source]) for destination in all_nodes]for source in all_nodes]

# print(adjacency_matrix)

# part 1 
def count_paths(graph, current_node, target_node):
    if current_node == target_node:
        return 1
    
    total_paths = 0

    for neighbor in graph[current_node]:
        total_paths += count_paths(graph, neighbor, target_node)

    return total_paths

result = count_paths(graph, "you", "out")
print(result)

# part 2
@lru_cache(None)
def count_paths(current_node, visited_fft, visited_dac):
    if current_node == "fft":
        visited_fft = True

    if current_node == "dac":
        visited_dac = True

    if current_node == "out":
        return 1 if visited_fft and visited_dac else 0
    
    return sum(count_paths(neighbor, visited_fft, visited_dac)for neighbor in graph[current_node])

result = count_paths("svr", False, False)
print(result)