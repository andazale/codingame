# https://www.codingame.com/ide/puzzle/dwarfs-standing-on-the-shoulders-of-giants

import sys
import math

n = int(input())  # the number of relationships of influence
edges = {}
for i in range(n):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    if n1 in edges:
        edges[n1].append(n2)
    else: edges[n1] = [n2]
    if n2 not in edges: edges[n2] = []

def dfs(graph, node, seen=None, path=None):
    if seen is None: seen = []
    if path is None: path = [node]

    seen.append(node)
    paths = []
    for t in graph[node]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(dfs(graph, t, seen[:], t_path))
    return paths

result = 0
for i in edges:
    if edges[i] != []:
        all_paths = dfs(edges, i)
        max_len = max(len(p) for p in all_paths)
        if max_len > result:
            result = max_len

# The number of people involved in the longest succession of influences
print(result)
