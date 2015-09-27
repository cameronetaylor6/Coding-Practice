from Queue import Queue as queue

class Queue(object):
	#A simple queue class, based on built-in python queue

	def __init__(self):
		self.q = queue(0)

	#add value to end of queue if value is an int and queue is not full
	def put(self, value):
		if not isinstance(value, int):
			print "Value is not an integer. Please use an integer."
			return False


		if self.q.full():
			print "Queue is full. Put failed."
			return False

		self.q.put(value)
		return True

	#get value from front of queue if queue is not empty
	def get(self):
		if self.q.empty():
			print "Queue is empty. Get failed."
			return False

		return self.q.get()

def QueueTest():
	#Test for queue
	print "Running Tests"
	print "Starting Queue testing"
	print "Putting Values"

	#create queue
	testQueue = Queue()

	#put values from 0 to 9 into the queue
	for i in range(0,10):
		print "Putting in value: {}".format(i)
		testQueue.put(i)

	#get the 10 values from the queue (should be order 0 to 9)
	print "Values put. Getting values"
	for i in range(0,10):
		print "Getting value: {}".format(testQueue.get())

	print "Queue testing finished."
	return True