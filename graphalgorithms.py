#
#   graphalgorithms.py
#
#   Author: Grant McGovern
#   Date: 26 April 2015
#
#   CSC 222 [] Lab 4 : Graph Exploration
#
#
#

import heapq
from Graphs.graph import *
from collections import deque
from Graphs.directedgraph import *

def dfs(g, start_node = None):
    """ Depth First Search for a graph. """
    
    if not start_node is None and not start_node in g.nodes():
        raise Exception('start node does not exist')
        
    visited = {}

    for node in g.nodes(): visited[node] = False
        
    if start_node is None: start_node = node
        
    item = deque([start_node])
    output = []
    
    while len(item) > 0:
        # Pop from the right (top of queue)
        node = item.pop()
        if not visited[node]:
            output.append(node)
            visited[node] = True
            for adj in g.neighbors(node):
                if not visited[adj]: item.append(adj)
    
    return output

def dijkstra(g, start_node, end_node=None):
    """ Finds the shortest path between two nodes"""
    
    _nodes_ = g.nodes()

    if not start_node in _nodes_: 
        pass
    if not end_node is None and not end_node in _nodes_: 
        pass
    
    distance = {}
    previous = {}
    
    for n in g.nodes():
        previous[n] = None
        distance[n] = float('inf')
        
    
    # Uses heap queue module
    distance_heap = []
    heapq.heappush(distance_heap, (0, start_node))
    
    while len(distance_heap) > 0:
        node_distance = heapq.heappop(distance_heap)        
        n = node_distance[1]
       
        if (node_distance[0]) >= (distance[n]): continue
        
        distance[n] = node_distance[0]
        
        if n == end_node: break
        
        for adj in g.weighted_neighbors(n):
            adj_node = adj[0]
            edge_weight = adj[1]

            if edge_weight < 0: raise Exception('Cannot perform Dijkstra\'s algorithm on negative edges') 
            
            new_distance = distance[n] + edge_weight
            
            if distance[adj_node] > new_distance:
                previous[adj_node] = n
                heapq.heappush(distance_heap, (new_distance, adj_node))
                
    if end_node is None: 
        return (distance, previous)
    else:
        return (distance[end_node], previous)


def incomingEdges(g):
    if isinstance(g, Graph):
        raise Exception('spanning tree not defined for undirected graphs')

    # Count the number of incoming edges to each node
    num_incoming = {}

    for node in g.nodes():
        num_incoming[node] = 0
    for edge in g.edges():
        print edge[1]
        num_incoming[edge[1]] += 1

    return num_incoming
        
def components(g):
    return g.components()
