'''
A program by Nate Weeks to implement prims algorith to find a minimum spanning tree
on a connected, undirected, weighted graph.
March 2019
https://coderbyte.com/algorithm/find-minimum-spanning-tree-using-prims-algorithm
'''

from minheapvertex import MinHeapVertex
import random

graph = {'a': {'b': 1, 'c': 2, 'd': 1},
    'b': {'a': 1, 'e': 2, 'f': 1},
    'c': {'a': 1, 'f': 2, 'g': 1, 'h': 2},
    'd': {'a': 1, 'h': 1},
    'e': {'b': 2},
    'f': {'b': 1, 'c': 2, 'g': 2},
    'g': {'c': 1, 'f': 2},
    'h': {'c': 2, 'd': 1}}

def createGraph(size):
    ''' given a size, create a connected graph with random connections/weights'''
    graph = {}
    # create the base entries
    for num in range(size+1):
        graph[num] = {}
    # make sure the graph has at least 1 connection between each vertex
    for num in range(size):
        graph[num] = {num + 1: random.randint(1,100)}
    # add in random connections between random
    for x in range(size):
        new = {}
        start = random.randint(0,size-1)
        dest = random.randint(0,size-1)
        distance = random.randint(1, 100)
        new[dest] = distance
        graph[start].update(new)
    return graph

def prims(graph):
    vertex = 0
    minimumTree = []
    edges = []
    visited = []
    minimumEdge = [None, None, float('inf')]

    while len(minimumTree) < len(graph) - 1:
        visited.append(vertex)
        # add the edges adjacent to a given vertex
        for point in graph[vertex]:
            edges.append([vertex, point, graph[vertex][point]])
        # find edge with the smallest weight to a vertex
        # that has not yet been visited
        for point in range(len(edges)):
            if edges[point][2] < minimumEdge[2] and edges[point][1] not in visited:
                minimumEdge = edges[point]

        # remove the minimum edge
        edges.remove(minimumEdge)

        minimumTree.append(minimumEdge)

        vertex = minimumEdge[1]
        # reset the minimumEdge
        minimumEdge = [None, None, float('inf')]

    return minimumTree

def primsMinheap(graph):
    vertex = 0
    minimumTree = []
    edges = MinHeapVertex([])
    visited = []
    minimumEdge = [None, None, float('inf')]

    while len(minimumTree) < len(graph) - 1:
        visited.append(vertex)
        # add the edges adjacent to a given vertex
        for point in graph[vertex]:
            edges.push([vertex, point, graph[vertex][point]])
        # find edge with the smallest weight to a vertex
        # that has not yet been visited
        # edge[0] = start edge[1] = dest edge[2] = distance
        while True:
            edge = edges.pop()
            if edge[2] < minimumEdge[2] and edge[1] not in visited:
                minimumEdge = edge
                break

        minimumTree.append(minimumEdge)

        vertex = minimumEdge[1]
        # reset the minimumEdge
        minimumEdge = [None, None, float('inf')]

    return minimumTree
print(len(graph))
# primsMinheap(createGraph(2000))
# prims(createGraph(3000))
