from Linked_Node import Node

class Linked_List(object):
	def __init__(self, value):
		self.head = Node(value)

	def getHead(self):
		return self.head

	def addToTail(self, value):
		current = self.getHead()
		while(current.getNext() is not None):
			current = current.getNext()
		current.setNext(Node(value))

	def findValue(self, value):
		current = self.getHead()
		while(current.getNext() is not None):
			if(current.getData() == value):
				return True
			else:
				current = current.getNext()
		if(current.getData() == value):
			return True
		else:
			return False

	def removeValue(self, value):
		current = self.getHead()
		if(current.getData() is value):
			self.head = current.getNext()
			del current
			return
		while(current.getNext().getNext() is not None and current.getNext().getData() is not value):
			current = current.getNext()
		if(current.getNext().getData() is value):
			if(current.getNext().getNext() is None):
				next = current.getNext()
				current.setNext(None)
				del next
			else:
				next = current.getNext()
				current.setNext(next.getNext())
				del next

	def printList(self):
		current = self.getHead()
		while(current.getNext() is not None):
			print(current)
			current = current.getNext()
		print(current)

if __name__ == "__main__":
	a = Linked_List(5)
	a.addToTail(6)
	a.addToTail(7)
	a.addToTail(7)
	a.addToTail(3)
	a.addToTail(2)
	a.printList()
	a.removeValue(7)
	a.removeValue(2)
	a.printList()
	a.removeValue(5)
	a.printList()
	print(a.findValue(7))
	print(a.findValue(5))