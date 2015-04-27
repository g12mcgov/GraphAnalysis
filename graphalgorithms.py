#!/usr/local/bin/python

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
from collections import deque
from Graphs.directedgraph import DirectedGraph

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
    
    for node in g.nodes():
        previous[node] = None
        distance[node] = float('inf')
        
    
    # Uses heap queue module
    distance_heap = []
    heapq.heappush(distance_heap, (0, start_node))
    
    while len(distance_heap) > 0:
        node_distance = heapq.heappop(distance_heap)        
        node = node_distance[1]
       
        if (node_distance[0]) >= (distance[node]): continue
        
        distance[node] = node_distance[0]
        
        if node == end_node: break
        
        for adj in g.weighted_neighbors(node):
            adj_node = adj[0]
            edgeWeight = adj[1]

            if edgeWeight < 0: raise Exception('Cannot perform Dijkstra\'s algorithm on negative edges') 
            
            new_distance = distance[node] + edgeWeight
            
            if distance[adj_node] > new_distance:
                previous[adj_node] = node
                heapq.heappush(distance_heap, (new_distance, adj_node))
                
    if end_node is None:
        return (distance, previous)
    else:
        return (distance[end_node], previous)


def incomingEdges(g):
    if isinstance(g, Graph):
        raise Exception("This does not work for undirected graphs")

    # Count the number of incoming edges to each node
    incoming = {}

    for node in g.nodes(): incoming[node] = 0
    for edge in g.edges():
        print edge[1]
        incoming[edge[1]] += 1

    return incoming
