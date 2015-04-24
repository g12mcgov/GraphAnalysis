import copy
from graphalgorithms import *
from collections import deque
from Graphs.directedgraph import DirectedGraph

def main():
    filedata = readFile("FBdata.txt")
    graph = generateUndirectedGraph(filedata)
    
    # This is stupid, but why not
    componentsLength = lambda graph: len(graph.components())
    
    print componentsLength(graph)


def getDegrees(graph, nodes):
    """ Returns a list of indegree/outdegree of a graph """
    outdegree = 0
    indegree = 0

    node_list = []

    for node in nodes:
        node_info = {}

        for item in graph.edges():
            if item[0] == node:
                outdegree += 1
            if item[1] == node:
                indegree +=1 

        node_info["node"] = node
        node_info["outdegree"] = outdegree
        node_info["indegree"] = indegree

        node_list.append(node_info)

        indegree = outdegree = 0

    return node_list

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
        vertices = [str(vertex.strip("\n")) for vertex in listifiedFile][0:numVertices+1]
        fp.close()
    # File buffer expires, reload the file to get edges
    with open(filename) as fp2:
        preEdges = list(fp2)[numVertices+3:]
        edges = [tuple(edge.strip("\n").split(" ")) for edge in preEdges]
        fp2.close()

    return {"numVertices": numVertices, "vertices": vertices, "edges": edges}

def generateUndirectedGraph(filedata):
    """ Creates a bidirectional graph """
    graph = DirectedGraph()

    edges = filedata["edges"]
    # Combine the edges with the reversed edges to get a bidirectional graph
    edgescombined = [(edge[0], edge[1], 1) for edge in edges] + [(edge[0], edge[1], 1) for edge in edges]
    graph.add_weighted_edges(edgescombined)

    return graph



if __name__ == "__main__":
    main()
