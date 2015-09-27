import random

class BinaryTree(object):
	#Simple binary tree, made up of nodes

	def __init__(self, value):
		self.root = Node(value)

	#adds node of value to node of parentValue if parent has open children spot and value doesn't exist already
	def add(self, value, parentValue):
		if not isinstance(value, int):
			print "Value is not an integer. Please use an integer."
			return False
		if not isinstance(parentValue, int):
			print "Parent value is not an integer. Please use an integer."
			return False

		#find parent and children, fail if parent doesn't exist or if child does
		parent = self.searchChildren(self.root, parentValue)
		child = self.searchChildren(self.root, value)

		if child != False:
			print "Value already in tree. Please use a unique value."
			return False

		if parent == False:
			print "Parent not found."
			return False

		if parent.left != None and parent.right != None:
			print "Parent has two children, node not added."
			return False

		#add child node to parent in open spot (left > right)
		if parent.left == None:
			parent.left = Node(value)
			parent.left.parent = parent
			return True

		if parent.right == None:
			parent.right = Node(value)
			parent.right.parent = parent
			return True

	#prints the tree starting at the root
	def printTree(self):
		self.printNodes(self.root)

	#recursive print that takes in a node, prints node and then recurses through children
	def printNodes(self, node):
		if not isinstance(node, Node):
			print "Node is not an node."
			return False

	 	print(node.data)

	 	#recurse through children, printing their children if they exist
	 	if node.left != None:
	 		self.printNodes(node.left)
	 	if node.right != None:
			self.printNodes(node.right)

	 	return True

	#deletes node of value if it exists and has no children
	def delete(self,value):
		if not isinstance(value, int):
	 		print "Value is not an integer. Please use an integer."
	 		return False

	 	#find node in graph, exit if it doesn't exist
	 	delete = self.searchChildren(self.root, value)
	 	if delete == False:
	 		print "Node not found."
	 		return False

	 	if delete.left != None or delete.right != None:
	 		print "Node not deleted, has children"
	 		return False
	 	
	 	#set node's data to none
	 	delete.data = None

	 	#find out which child the node is, remove link and delete instance
	 	if(delete.parent.left == delete):
	 		delete.parent.left = None
	 		del delete
	 		return True
	 	if(delete.parent.right == delete):
	 		delete.parent.right = None
	 		del delete
	 		return True

	#search through graph for a node of value, node is the starting point for recursion
	def searchChildren(self, node, value):
		if not isinstance(node, Node):
			print "Node is not an node."
			return False
		if not isinstance(value, int):
	 		print "Value is not an integer. Please use an integer."
	 		return False

	 	#if our node's data equal our value, we're done
	 	if node.data == value:
	 		return node

	 	#clean this up?
	 	#if we find our node recursively in the children, return it, otherwise exit with false
	 	found = False

	 	if node.left != None:
	 		found = self.searchChildren(node.left, value)
	 	if found != False:
	 		return found

	 	if node.right != None:
			found = self.searchChildren(node.right, value)
		if found != False:
	 		return found

	 	return 

def BinaryTest():
	#binary tree test

	#variable for storing parent value, random int to delete node
	j = 0
	print "Starting Binary Tree testing"
	print "Adding Nodes"

	#create tree with root node of 0
	testTree = BinaryTree(0)

	#adding nodes 1 to 9
	for i in range(1, 10):
		print "Adding node: {} to parent node: {}".format(i, j)
		j = ((i+1)/2)-1
		testTree.add(i, j)

	#print the tree as is
	print "Nodes added. Printing tree."
	testTree.printTree()

	#deleting nodes randomly, maximum of 9
	print "Tree printed. Deleting nodes."
	for i in range(0,9):
		j = random.randint(0,9)
		print "Deleting node: {}".format(j)
		testTree.delete(j)

	print "Nodes deleted. Printing tree."
	testTree.printTree()


	print "Tree testing finished."
	return True