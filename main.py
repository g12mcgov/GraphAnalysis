#
#   main.py
#
#   Author: Grant McGovern
#   Date: 26 April 2015
#
#   CSC 222 [] Lab 4 : Graph Exploration
#
#
#

import copy
from graphalgorithms import *
from collections import deque
from Graphs.directedgraph import DirectedGraph

def main():
    # Problem 1
    print "\nProblem #1:\n"
    filedata = readFile("FBdata.txt")
    graph = generateUndirectedGraph(filedata)
    vertices = filedata["vertices"]

    degrees = getDegrees(graph, vertices)

    # Finds the max interaction
    maxInteraction = max(degrees, key=lambda indegree:indegree['indegree'])
    sumOfIndegrees = sum(indegree['indegree'] for indegree in degrees)
    averageIndegrees = sumOfIndegrees / float(len(vertices))

    print "Most interacted Node: %s" % maxInteraction["node"]
    print "Indegree: %s\n" % maxInteraction["indegree"]
    print "Average Interactions (# of Edges): %s" % averageIndegrees
    print "Average Interactions (Two interaction per edge): %s" % (averageIndegrees / 2)

    maximumStronglyConnectedComponents = max([len(scc) for scc in graph.components()])

    print "Largest Subgroup of Users: %s" % maximumStronglyConnectedComponents
    
    # Problem 2
    print "\nProblem #2:\n"
    filedata = readFile("cswebData.txt")
    graph = generateDirectedGraph(filedata)
    vertices = filedata["vertices"]

    degrees = getDegrees(graph, vertices)
    
    # Compute in/out degrees of largest node
    maxIndegree = max(degrees, key=lambda indegree:indegree['indegree'])
    maxOutdegree = max(degrees, key=lambda outdegree:outdegree['outdegree'])

    print "Web Page w/ Most Incoming Links: %s" % maxIndegree["node"]
    print "Web Page w/ Most Outgoing Links: %s" % maxOutdegree["node"]

    maximumStronglyConnectedComponents = max([len(scc) for scc in graph.components()])

    print "Largest Cycle: %s" % str(maximumStronglyConnectedComponents)

    startNode = "http://www.wfu.edu"
    endNode = "http://csweb.cs.wfu.edu"

    # Compute shortest path
    shortestPath = dijkstra(graph, startNode, end_node=endNode)[0]

    bonus_question = "\nBonus: "
    if shortestPath == float('Inf'):
        print bonus_question + "Path Does Not Exist"
    else:
        print bonus_question + "Shortest Path (len): " + str(shortestPath)


def getDegrees(graph, nodes):
    """ Returns a list of indegree/outdegree of a graph """
    outdegree = 0
    indegree = 0

    nodeDictList = []

    for node in nodes:
        degrees = {}

        edges = graph.edges()

        for edge in edges:
            if edge[0] == node: outdegree += 1
            if edge[1] == node: indegree +=1 

        degrees["node"] = node
        degrees["outdegree"] = outdegree
        degrees["indegree"] = indegree

        nodeDictList.append(degrees)

        indegree = 0
        outdegree = 0

    return nodeDictList

def printNodes(nodes):
    """ Prints all of the nodes in the graph and their neighbors """
    for node in nodes:
        print "Node: ", node
        neighbors = g.neighbors(node)
        for item in neighbors:
            print item

def readFile(filename):
    """ Reads in the filename and returns dictionary of graph info """
    with open(filename) as fp:
        listifiedFile = list(fp)
        numVertices = int(listifiedFile[0].strip("\n"))
        vertices = [str(vertex.rstrip().strip("\n")) for vertex in listifiedFile][1:numVertices+1]
        fp.close()
    # File buffer expires, reload the file to get edges
    with open(filename) as fp2:
        preEdges = list(fp2)[numVertices+3:]
        edges = [tuple(edge.rstrip().strip("\n").split(" ")) for edge in preEdges]
        fp2.close()

    return {"numVertices": numVertices, "vertices": vertices, "edges": edges}

def generateUndirectedGraph(filedata):
    """ Creates a bidirectional graph """

    graph = DirectedGraph()

    edges = filedata["edges"]
    # Combine the edges with the reversed edges to get a bidirectional graph
    edgescombined = [(edge[0], edge[1], 1) for edge in edges] + [(edge[1], edge[0], 1) for edge in edges]
    graph.add_weighted_edges(edgescombined)

    return graph

def generateDirectedGraph(filedata):
    """ Creates a directional graph """

    graph = DirectedGraph()

    edges = filedata["edges"]

    oneWayEdges = [(edge[1], edge[0], 1) for edge in edges]
    graph.add_weighted_edges(oneWayEdges)

    return graph


if __name__ == "__main__":
    main()
