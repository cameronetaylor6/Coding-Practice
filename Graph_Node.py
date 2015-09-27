import random

class Node(object):
	#Simple node class

	def __init__(self, value):
		if not isinstance(value, int):
			print "Value is not an integer. Please use an integer."
			raise TypeError

		self.data = value
		self.left = None
		self.right = None
		self.parent = None

class Graph(object):
	#Simple graph class using dictionary

	def __init__(self):
		self.data = {}

	#adds a vertex with to graph if value is an int and that verteix doesn't exist already
	def addVertex(self, value):
		if not isinstance(value, int):
			print "Value is not an integer. Please use an integer."
			return False

		if value in self.data.keys():
			print "Value already exists."
			return False

		self.data[value] = []
		return True

	#adds an edge between the vertices of value1 and value2 if both exist, are not the same value, and don't already share an edge
	def addEdge(self, value1, value2):
		if value1 not in self.data.keys() or value2 not in self.data.keys():
			print "One or more vertices not found."
			return False

		if value1 == value2:
			print "Values are same. Please use two different values."
			return False

		if value2 in self.data[value1] or value1 in self.data[value2]:
			print "Vertices already share an edge."
			return False

		self.data[value1].append(value2)
		self.data[value2].append(value1)
		return  True

	#prints all edges of vertex with value
	def findVertex(self, value):
		if value not in self.data.keys():
			print "Value not found."
			return False

		for adj in self.data[value]:
			print(adj)

		return True

def GraphTest():
	#graph test

	#variables for storing random ints for edge testing later
	j = 0
	k = 0
	print "Starting Graph testing"
	print "Adding Vertices"

	#create Graph
	testGraph = Graph()

	#add vertices 0 to 9
	for i in range(0,10):
		print "Adding Vertex: {}".format(i)
		testGraph.addVertex(i)

	#attempt to add in 35 edges randomly - some will be duplicates and won't be added
	print "Verteces added. Adding Edges."
	for i in range(0,35):
		j = random.randint(0,9)
		k = random.randint(0,9)
		while(j == k):
			k = random.randint(0,9)
		print "Adding edge: {}, {}".format(j, k)
		testGraph.addEdge(j, k)

	#print the adjacent vertices of the even vertices
	print "Edges added. Finding vertices"
	for i in range(0,5):
		print "Printing vertex: {}".format(2*i)
		testGraph.findVertex(2*i)

	print "Graph testing finished."
	return True