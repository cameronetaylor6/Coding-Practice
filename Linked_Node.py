class Node(object):
	def __init__(self, value):
		if not isinstance(value, int):
			print "Value is not an integer. Please use an integer."
			raise TypeError

		self.data = value
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setNext(self, newNext):
		self.next = newNext

	def __str__(self):
		return("Value: " + str(self.data))

if __name__ == "__main__":
	a = Node(5)
	a.setNext(Node(6))
	print(a)
	print(a.getNext())