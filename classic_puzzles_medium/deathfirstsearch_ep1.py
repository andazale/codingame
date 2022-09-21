# https://www.codingame.com/ide/puzzle/death-first-search-episode-1

import sys
import random

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
edges = {}
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    if n1 in edges:
        edges[n1].append(n2)
    else: edges[n1] = [n2]
    if n2 in edges: edges[n2].append(n1)
    else: edges[n2] = [n1]
indexes = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    indexes.append(ei)
print(indexes, file=sys.stderr, flush=True)


def dijkstra(current):
    unvisited = {node: None for node in range(n)}
    visited = {}
    current_distance = 0
    unvisited[current] = current_distance

    while True:
        for neighbor in edges[current]:
            if neighbor not in unvisited: continue
            new_distance = current_distance + 1
            if unvisited[neighbor] is None or unvisited[neighbor] > new_distance:
                unvisited[neighbor] = new_distance
        visited[current] = current_distance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, current_distance = sorted(candidates, key = lambda x: x[1])[0]
    return visited

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    distances = dijkstra(si)
    del distances[si]
    
    temp = min(distances.values())
    result = [key for key in distances if distances[key] == temp]
    node2 = random.choice(result)
    for i in result:
        if i in indexes:
            node2 = i

    # indices of the nodes you wish to sever the link between
    print(si, node2)
