class Stack(object):
	#A simple stack class

	def __init__(self):
		self.data = []

	#push value onto stack if value is an int
	def push(self, value):
		if not isinstance(value, int):
			print "Value is not an integer. Please use an integer."
			return False

		self.data.append(value)
		return True

	#pop value off of stack if stack has at least one value
	def pop(self):
		if len(self.data) <= 0:
			print "Stack is empty. Pop failed."
			return False

		return self.data.pop()

	def checkSize(self):
		return len(self.data)

def StackTest():
	#test for stack
	print "Starting Stack testing"
	print "Pushing Values"

	#create stack
	testStack = Stack()

	#push values 0 to 9 to the stack
	for i in range(0,10):
		print "Pushing value: {}".format(i)
		testStack.push(i)

	#pop all 10 values from the stack (should be ordered 9 to 0)
	print "Values pushed. Popping values"
	for i in range(0,10):
		print "Popping value: {}".format(testStack.pop())

	print "Stack testing finished."
	return True