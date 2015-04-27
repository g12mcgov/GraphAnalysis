#!/usr/local/bin/python

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

# Module imports
from collections import deque
from termcolor import colored, cprint

# Local imports
from Graphs.directedgraph import DirectedGraph
from graphalgorithms import dfs, dijkstra, incomingEdges

def main():
    # Problem 1
    print "\nProblem #1:\n"
    filedata = readFile("FBdata.txt")
    graph = generateUndirectedGraph(filedata)
    vertices = filedata["vertices"]

    # Get node information list
    degrees = getDegrees(graph, vertices)

    # Finds the max interaction
    maxInteraction = max(degrees, key=lambda indegree:indegree['indegree'])
    sumOfIndegrees = sum(indegree['indegree'] for indegree in degrees)
    averageIndegrees = (sumOfIndegrees / float(len(vertices)))

    print "Most interacted Node: %s" % colored(maxInteraction["node"], 'green')
    print "Indegree: %s\n" % colored(maxInteraction["indegree"], 'green')
    print "Average Interactions (# of Edges): %s" % colored(averageIndegrees, 'green')
    print "Average Interactions (Two interaction per edge): %s" % colored((averageIndegrees / 2), 'green')

    maximumStronglyConnectedComponents = max([len(scc) for scc in graph.components()])

    print "Largest Subgroup of Users: %s" % colored(maximumStronglyConnectedComponents, 'green')
    
    # ---------------------------------------------------------------------------------#

    # Problem 2
    print "\nProblem #2:\n"
    filedata = readFile("cswebData.txt")
    graph = generateDirectedGraph(filedata)
    vertices = filedata["vertices"]

    # Get node information list
    degrees = getDegrees(graph, vertices)
    
    # Compute in/out degrees of largest node
    maxIndegree = max(degrees, key=lambda indegree:indegree['indegree'])
    maxOutdegree = max(degrees, key=lambda outdegree:outdegree['outdegree'])

    print "Web Page w/ Most Incoming Links: %s" % colored(maxIndegree["node"], 'green')
    print "Web Page w/ Most Outgoing Links: %s" % colored(maxOutdegree["node"], 'green')

    maximumStronglyConnectedComponents = max([len(scc) for scc in graph.components()])

    print "Largest Cycle: %s" % colored(str(maximumStronglyConnectedComponents), 'green')

    # Our nodes to find paths between
    startNode = "http://www.wfu.edu"
    endNode = "http://csweb.cs.wfu.edu"

    # Compute shortest path
    shortestPath = dijkstra(graph, startNode, end_node=endNode)[0]

    bonus_question = "\nBonus: "
    if shortestPath == float('Inf'):
        print bonus_question + colored("Path Does Not Exist", 'red')
    else:
        print bonus_question + "Shortest Path (len): " + colored(str(shortestPath), 'green')


def printNodes(nodes):
    """ Prints all of the nodes in the graph and their neighbors """
    for node in nodes:
        print "Node: ", node
        neighbors = g.neighbors(node)
        for neighbor in neighbors:
            print neighbor

def readFile(filename):
    """ Reads in the filename and returns dictionary of graph info """
    with open(filename) as file1:
        listifiedFile = list(file1)
        numVertices = int(listifiedFile[0].strip("\n"))
        # Cleans up the file, getting rid of new lines and '\r' character
        vertices = [str(vertex.rstrip().strip("\n")) for vertex in listifiedFile][1:numVertices+1]
        file1.close()

    # File buffer expires, reload the file to get edges
    with open(filename) as file2:
        preEdges = list(file2)[numVertices+3:]
        # Cleans up the file, getting rid of new lines and '\r' character
        edges = [tuple(edge.rstrip().strip("\n").split(" ")) for edge in preEdges]
        file2.close()

    return { 
    "numVertices": numVertices, 
    "vertices": vertices, 
    "edges": edges 
    }

def generateUndirectedGraph(filedata):
    """ Creates a bidirectional graph """

    graph = DirectedGraph()

    edges = filedata["edges"]
    # Combine the edges with the reversed edges to get a bidirectional graph
    edgescombined = [(edge[0], edge[1], 1) for edge in edges] + [(edge[1], edge[0], 1) for edge in edges]
    graph.add_weighted_edges(edgescombined)

    return graph

def generateDirectedGraph(filedata):
    """ Creates a one-directional graph """

    graph = DirectedGraph()

    edges = filedata["edges"]

    oneWayEdges = [(edge[1], edge[0], 1) for edge in edges]
    graph.add_weighted_edges(oneWayEdges)

    return graph

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


if __name__ == "__main__":
    main()
