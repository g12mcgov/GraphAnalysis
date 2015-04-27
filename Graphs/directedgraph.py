#!/usr/local/bin/python

#
#   directedgraph.py
#
#   Author: Grant McGovern
#   Date: 26 April 2015
#
#   CSC 222 [] Lab 4 : Graph Exploration
#
#
#

import sys
import copy

# Append one directory up to get our graphalgorithms package
sys.path.append("../")

# This is horrible Python import code
from collections import deque
from GraphProject.graphalgorithms import dfs, dijkstra, incomingEdges

class DirectedGraph:
    """ Class definition for a directed graph. """

    def __init__(self, graph=None):
        if graph is None or not graph:
            self.vertices = self._edges = {}
        else:
            self.vertices = copy.deepcopy(graph.vertices)
            self._edges = copy.deepcopy(graph._edges)
    
    def add_node(self, n):
        self.vertices[n] = {}
        self._edges[n] = {}
            
    def addvertices(self, nodes):
        """ Adds nodes to the graph """
        for n in nodes: self.add_node(n)
    
    def add_edges(self, edges):
        """ Adds edges to graph, but also to nodes if they don't already exist """
        for edge in edges:
            if not edge[0] in self.vertices: self.add_node(edge[0])
            if not edge[1] in self.vertices: self.add_node(edge[1])

            self._edges[edge[0]][edge[1]] = 1

    def add_weighted_edges(self, edges):
        for edge in edges:
            if not edge[0] in self.vertices: self.add_node(edge[0])
            if not edge[1] in self.vertices: self.add_node(edge[1])
            
            self._edges[edge[0]][edge[1]] = edge[2]        

    def edge_weight(self, edge):
        if edge[0] in self._edges and edge[1] in self._edges[edge[0]]:
            return self._edges[edge[0]][edge[1]]
        else:
            raise AttributeError('edge does not exist')
        
    ### One liner methods ###

    # Get number of vertices
    def numVertices(self): return len(self.vertices)

    # Get all the nodes
    def nodes(self): return iter(self.vertices.keys())

    # Get all neighboring nodes
    def neighbors(self, node): return iter([n[0] for n in self._edges[node].iteritems()])

    # Get all of the weights for each neighbor (will all be 1 in our case)
    def weighted_neighbors(self, node): return self._edges[node].iteritems()

    # Overrides built-in length method
    def __len__(self): return len(self.vertices)

    # Gets number of edges in the graph
    def num_edges(self):
        number = 0
        for n, neighbors in self._edges.iteritems():
            number += len(neighbors)
        
        return number


    def edges(self):
        """ Returns iterator over edges """
        for node, neighbors in self._edges.iteritems():
            for neigh, w in neighbors.iteritems():
                yield (node, neigh, w)
                
    
    def transpose(self):
        """ Returns the transpose of the graph. """
        
        graph = DirectedGraph()
        for node in self.nodes(): graph.add_node(node)
        
        new_edges = [(edge[1], edge[0], edge[2]) for edge in self.edges()]
        
        graph.add_weighted_edges(new_edges)
        
        return graph
    
    def components(self):
        """Finds the strongly connected components of the graph. """
        
        comps = []
        reversed_ = self.transpose()
        
        queue = deque(self.nodes())

        visited = {}

        for n in self.nodes(): visited[n] = False
        
        while len(queue) > 0:
            n = queue.pop()
            if not visited[n]: 
                c = dfs(self, n)
                reversed_components = dfs(reversed_, n)
                tmp_comp = []
                
                for adj in c:
                    if adj in reversed_components:
                        visited[adj] = True
                        tmp_comp.append(adj)
                
                comps.append(tmp_comp)
        
        return comps
