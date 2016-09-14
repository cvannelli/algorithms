import numpy as np
import math, re, sys
import networkx as nx
from operator import itemgetter
import os
import time


# Holds vertex data and returns distance between vertices
class City:
	# initializes a city with it's line number, x, and y coordinates.
	def __init__(self, number, x, y):
		self.node = number
		self.x = x
		self.y = y

	# returns x coordinate
	def returnX(self):
		return self.x

	# returns y coordinate
	def returnY(self):
		return self.y

	# returns city number
	def returnNode(self):
		return self.node

	# calculates the distance between vertices
	def distance(self, City):
		dx = abs(self.returnX() - City.returnX())
		dy = abs(self.returnY() - City.returnY())

		distance = int(round(math.sqrt((dx * dx) + (dy * dy)), 0))

		return distance


# Holds a list of the vertices and returns vertices
class CityList:
	# holds the list of vertices
	destinations = []

	# function adds vertices
	def addCity(self, City):
		self.destinations.append(City)

	# returns the length of the list of vertices
	def cityCount(self):
		return len(self.destinations)

	# returns the vertex specified at index of the list
	def returnCity(self, index):
		return self.destinations[index]


# Initializes a CityList into a complete graph, returns the graph and also MST of the graph.
class Graph:
	# initializes object containing a complete graph of the vertices with weights
	def __init__(self, cityList):
		self.size = cityList
		self.cityList = cityList
		self.graph = nx.complete_graph(self.cityList.cityCount())

		for i in range(0, self.cityList.cityCount()):
			for j in range(0, self.cityList.cityCount()):
				if i != j:
					self.graph.edge[i][j]['weight'] = self.cityList.returnCity(i).distance(self.cityList.returnCity(j))

	# returns the complete graph
	def returnGraph(self):
		return self.graph

	# returns the minimum spanning tree
	def MST(self):
		T = nx.minimum_spanning_tree(self.graph)
		return T

# function obtains odd degree vertices
def getOdds(MST):
	oddList = []
	for i in range(0, len(MST.nodes())):
		if (MST.degree(i) % 2 != 0):
				oddList.append(i)
	return oddList


# Class helps convert the MST into a minimum matching multigraph
class PerfectMatch:
	def __init__(self, oddList, completeGraph, MST):
		self.MST = MST
		self.oddList = oddList
		self.completeGraph = completeGraph
		self.oddGraph = self.completeGraph.subgraph(oddList)
		self.multigraph = nx.MultiGraph()
		self.multigraph.add_nodes_from(MST)

		self.mstEdges = list(self.MST.edges())
		self.weights = []

		for i in range(0, len(self.mstEdges)):
			self.weights.append(self.MST[self.mstEdges[i][0]][self.mstEdges[i][1]]["weight"])

		for i in range(0, len(self.mstEdges)):
			self.multigraph.add_edge(self.mstEdges[i][0], self.mstEdges[i][1], weight=self.weights[i])

	# find the min weight matching of the odd vertices and appends
	# the edges to the MST in the form of a multigraph
	def edges(self):
		for v1, v2 in self.oddGraph.edges_iter():
			self.oddGraph[v1][v2]["weight"] = -(self.oddGraph[v1][v2]["weight"])

		edges = nx.max_weight_matching(self.oddGraph, maxcardinality=True)

		for v1, v2 in self.oddGraph.edges_iter():
			self.oddGraph[v1][v2]["weight"] = -(self.oddGraph[v1][v2]["weight"])

		edgeList = list(edges.items())

		weights = []

		for i in range(0, len(edgeList)):
			weights.append(self.oddGraph[edgeList[i][0]][edgeList[i][1]]["weight"])

		for i in range(0, len(edgeList)):
			for j in range(i, len(edgeList)):
				if edgeList[i][0] == edgeList[j][1]:
					self.multigraph.add_edge(edgeList[i][0], edgeList[i][1], weight=weights[i])

		return(self.multigraph)


# Based upon readInstance Function provided in verification files.
def readinstance(filename):

    f = open(filename, 'r')
    line = f.readline()
    cityList = CityList()
    x = 0
    while len(line) > 1:
        lineparse = re.findall(r'[^,;\s]+', line)
        city = City(x, int(lineparse[1]), int(lineparse[2]))
        cityList.addCity(city)
        x = x + 1
        line = f.readline()
    f.close()
    return cityList


# function calculates euler path.
# based upon (euler.py networkx python module)
def Euler(G, source=None):
    g = G.__class__(G) # copies graph structure

    # set up the starting vertex
    if source is None:
        v = next(g.nodes_iter())
    else:
        v = source

    degree = g.degree
    edges = g.edges_iter
    get_city = itemgetter(1)

    stack = [v]
    last_city = None

    while stack:
        current_city = stack[-1]
        if degree(current_city) == 0:
            if last_city is not None:
                yield (last_city, current_city)
            last_city = current_city
            stack.pop()
        else:
            random_edge = next(edges(current_city))
            stack.append(get_city(random_edge))
            g.remove_edge(*random_edge)


# Helps convert the euler circuit into a readable form
# Uses list version of euler circuit to make a
# hamiltonian path
class EulerCircuit:
	def __init__(self, cir, cityList):
		self.cityList = cityList
		self.cir = list(cir)
		self.root = self.cir[0][0]
		self.path = []

		self.path.append(self.root)

		for i in range(0, len(self.cir)):
			self.path.append(self.cir[i][1])

	# prints the euler circuit
	def printList(self):
		print(self.path)

	# returns the hamilton path of the euler circuit
	def hamilton(self):
		visited = np.zeros(self.cityList.cityCount())
		hamPath = []

		for i in range(0, len(self.path)):
			if visited[self.path[i]] == 0:
				hamPath.append(self.path[i])
				visited[self.path[i]] = 1

		distance = tspDistance(hamPath, self.cityList)

		return(hamPath, distance)


# Calculates the total distance traveled in the hamiltonian circuit
def tspDistance(ham, cityList):
	total = 0

	for i in range(0, len(ham) - 1):
		total += cityList.returnCity(ham[i]).distance(cityList.returnCity(ham[i + 1]))

	total += cityList.returnCity(ham[len(ham) - 1]).distance(cityList.returnCity(ham[0]))

	return(total)


# Function: distance(int, int)
# Description: Calculate Distance Between 2 Vertices
# Reference: tsp-verifier.py
# NOTE: Returns the distance, rounded to the nearest int

def getdistance(vert1, vert2):
	dx = vert1[0] - vert2[0]
	dy = vert1[1] - vert2[1]
	return int(round(math.sqrt(dx * dx + dy * dy)))


# Function: getgreedyTSP(int array[], int)
# Description: Calculates the "Nearest Neighbor" Shortest Path
# Using an Array of Vertices and a Starting Vertex
# NOTE: This will be called only once for the singleStart greedy method

def getgreedyTSP(vertices, startV):
	# Initialize total path distance to 0
	pathDistance = 0
	# Initialize array of unvisited vertices as all
	unvisited = [vertex for vertex in vertices]
	# Remove the starting vertex
	unvisited.remove(startV)
	# Initialize path to include starting vertex
	path = []
	path.append(startV)
	# Initialize current vertex to starting vertex
	currV = startV

	# Loop until all cities have been included in tour
	while unvisited != []:
		# Initialize Nearest Neighbor to first vertex with a MAX distance
		nearestNB = (0, float("inf"))
		count = 0

		# Loop to find the nearest neighbor considering all unvisited vertices
		for vertex in unvisited:
			# Call to getDistance to calc distance between each unvisited neighbor
			distNB = getdistance(vertices[currV], vertices[vertex])
			count += 1
			# print("getGreedyTSP Iteration: %d") % (count)
			# Check if distance is less than currently stored nearest neighbor
			# if true, replace nearest neighbor
			if distNB < nearestNB[1]:
				nearestNB = (vertex, distNB)

		# Add the nearest neighbor to the path and remove from unvisited
		path.append(nearestNB[0])
		unvisited.remove(nearestNB[0])

		# Update pathDistance and set new current vertex to nearest neighbor
		pathDistance += nearestNB[1]
		currV = nearestNB[0]

	# Connect last vertex with starting vertex to complete the path
	pathDistance += getdistance(vertices[startV], vertices[nearestNB[0]])
	print("DONE!")

	# return the pathDistance and path array
	return (path, pathDistance)
