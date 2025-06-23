from collections import defaultdict
import time

# Parse the edge list and build adjacency list
def build_graph(edge_list):
    graph = defaultdict(list)
    for edge in edge_list:
        u, v = edge.split(",")
        graph[u].append(v)
        graph[v].append(u)  # Since this is an undirected graph
    return graph

# BFS Implementation
def bfs_shortest_path(graph, start, target):
    visited = set()
    queue = [(start, 0)]  # (node, distance)
    visited.add(start)

    start_time = time.perf_counter_ns()
    while queue:
        current, distance = queue.pop(0)
        if current == target:
            return distance, time.perf_counter_ns() - start_time
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    return None, time.perf_counter_ns() - start_time # No path found

# DFS Implementation
def dfs_shortest_path(graph, start, target):
    visited = set()
    stack = [(start, 0)]  # (node, distance)
    visited.add(start)

    start_time = time.perf_counter_ns()
    while stack:
        current, distance = stack.pop()
        if current == target:
            return distance, time.perf_counter_ns() - start_time
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, distance + 1))
    return None, time.perf_counter_ns() - start_time # No path found

# Edge list provided in the prompt
edge_list = [
    "N_23,N_22", "N_15,N_10", "N_1,N_2", "N_12,N_7", "N_19,N_18",
    "N_10,N_15", "N_8,N_13", "N_17,N_22", "N_11,N_10", "N_2,N_1",
    "N_5,N_6", "N_10,N_5", "N_6,N_7", "N_13,N_14", "N_22,N_17",
    "N_24,N_19", "N_16,N_11", "N_9,N_8", "N_20,N_21", "N_6,N_1",
    "N_0,N_1", "N_14,N_13", "N_13,N_12", "N_2,N_3", "N_18,N_19",
    "N_15,N_20", "N_17,N_12", "N_4,N_9", "N_18,N_13", "N_13,N_18",
    "N_9,N_4", "N_7,N_6", "N_19,N_24", "N_10,N_11", "N_6,N_5",
    "N_13,N_8", "N_1,N_0", "N_21,N_20", "N_1,N_6", "N_20,N_15",
    "N_22,N_23", "N_7,N_12", "N_12,N_17", "N_11,N_16", "N_8,N_9",
    "N_5,N_10", "N_12,N_13", "N_3,N_2"
]

# Build the graph
graph = build_graph(edge_list)

# Nodes to evaluate
nodes = [f"N_{i}" for i in range(25)]

# Generate the report
results = []
start_node = "N_0"
for target_node in nodes:
    if start_node != target_node:
        bfs_result = bfs_shortest_path(graph, start_node, target_node)
        dfs_result = dfs_shortest_path(graph, start_node, target_node)
        if bfs_result[0] is not None:  # Path exists
            results.append({
                "Node 1": start_node,
                "Node 2": target_node,
                "BFS Distance": bfs_result[0],
                "BFS Time (ms)": bfs_result[1],
                "DFS Distance": dfs_result[0],
                "DFS Time (ms)": dfs_result[1],
            })

import pandas as pd

# Convert results to DataFrame
df = pd.DataFrame(results)

# Save to CSV
df.to_csv("social_network_analysis.csv", index=False)

# Display sample
print(df)
