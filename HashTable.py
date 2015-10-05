def hash_function(key_str, size):
	return sum([ord(c) for c in key_str]) % size

class HashTable:
	"""
	Hash table implementation that uses strings for keys.
	The value can be any object.
	Includes Python's dictionary interface.
	
	Usage:
	
	ht = HashTable(10)
	ht.set('a', 1).set('b', 2).set('c', 3)
	ht['c'] = 3
	
	"""
	def __init__(self, capacity=100):
		#default capacity is 100
		
		self.capacity = capacity
		self.size = 0
		self._keys = []
		#The hash table is stored in the form of: 
		#[ [ [key1, value], [key2, value] ], [ [key3, value] ] ]
		#The has function maps the index to the outermost list.
		#The innermost array is composed of the key and value.
		#The list of objects in each storage cell are listed in the middle-level arrays.
		self.data = [[] for _ in range(capacity)]
		
	def _find_by_key(self, key, find_result_func):
		index = hash_function(key, self.capacity)
		cell = self.data[index]
		found_item = None
		for item in cell:
			if item[0] == key:
				found_item = item
				break
				
		return find_result_func(found_item, cell)
		
	def set(self, key, obj):
	#Insert object into has table with key.
	#If key already exists, object will be updated.
	#Key must be a string.
		
		def find_result_func(found_item, cell):
			if found_item:
				found_item[1] = obj
			else:
				cell.append([key, obj])
				self.size += 1
				self._keys.append(key)
			
		self._find_by_key(key, find_result_func)
		return self
		
	def get(self, key):
	#Get object with key or raise KeyError if not found
	
		def find_result_func(found_item, _):
			if found_item:
				return found_item[1]
			else:
				raise KeyError(key)
				
		return self._find_by_key(key, find_result_func)
		
	def remove(self, key):
	#Remove the object associated with the given key.
	#If an object is found it will be returned, 
	#otherwise raise a KeyError
		
		def find_result_func(found_item, cell):
			if found_item:
				cell.remove(found_item)
				self._keys.remove(key)
				self.size -= 1
				return found_item[1]
			else:
				raise KeyError(key)
				
		return self._find_by_key(key, find_result_func)
		
	#Python's Dict Interface
	
	def keys(self):
		return self._keys
		
	def __setitem__(self, key, value):
		self.set(key, value)
		
	def __getitem__(self, key):
		return self.get(key)
		
	def __delitem__(self, key):
		return self.remove(key)
		
	#Computes the 'official' string representation of an object.
	def __repr__(self):
		return '{ ' + ', '.join([key + ':' + str(self.get(key)) for key in self._keys]) + ' }'

def HashTest():
	#Test for Hash Table
	print 'Running Tests'
	print 'Starting Hash Table Testing'
	
	#create Hash Table
	ht = HashTable()
	
	print 'Hash Table Successfully Created'
	print 'Inserting the values 1-5 into the hash table with respective keys a-e.'
	
	ht.set('a', 1).set('b', 2).set('c', 3).set('d', 4).set('e', 5)
	
	print 'Attempting to overwrite 1 by inserting the value 6 with the key, a.'
	
	ht.set('a', 6)
	
	print 'Checking the value with the key a. This should give 6 instead of 1.'
	
	print ht.get('a')
	
	print 'Removing the object associated with the key 'b'.'
	
	ht.remove('b')
	
	print 'Checking the remaining values to make sure they are still intact.'
	print 'This should return 6, 3, 4, 5 in sequence.'
	
	print ht.get('a')
	print ht.get('c')
	print ht.get('d')
	print ht.get('e')
	
	print 'Checking to make sure the object with key b (2) was successfully deleted.'
	print 'Testing is concluded and successful if this raises a KeyError.'
	
	print ht.get('b')
	
	return False
