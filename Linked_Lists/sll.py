class SLLNode:

	def __init__(self, data):
		self.data = data
		self.next = None

	def __repr__(self):
		return "SLLNode object: data={}".format(self.data)

	def get_data(self):
		"""Return the self.data attribute."""
		return self.data

	def set_data(self, new_data):
		"""Replace the existing value of the self.data attribute with new_data
		parameter."""
		self.data = new_data

	def get_next(self):
		"""Return the self.next attribute"""
		return self.next

	def set_next(self, new_next):
		"""Replace the existing value of the self.next attribute with new_next
		parameter."""
		self.next = new_next

class SLL:
	def __init__(self):
		self.head = None
	
	def __repr__(self) -> str:
		return "SLLNode object: head={}".format(self.head)
	
	def is_empty(self):
		return not self.head
	
	def add_front(self, new_data):
		"""Add a Node whose data is the new_data argument to the front of the SLL """
		temp = SLLNode(new_data)
		temp.set_next(self.head)
		self.head = temp

	def size(self):
		"""Traverses the SLL and returns an int value representing the number of nodes
		Time Complexity is O(n) because we need to visit each node in order to count it"""
		size = 0
		if self.is_empty():
			return 0
		current = self.head
		
		while current is not None:
			size += 1
			current = current.get_next()
		return size

	def search(self, data):
		"""Traverses the linked list and returns True if the data argument is
		present in one of the nodes. Otherwise, it returns False.
		Time Complexity is O(n) because we need to visit each node in order to count it"""
		if self.is_empty():
			return "Linked List is empty. No nodes to search."
		current = self.head
		while current is not None:
			if current.get_data() == data:
				return True
			current = current.get_next()
		return False

	def remove(self, data):
		"""Removes the first occurrence of a Node that contains the data argument
		as its self.data variable. Returns nothing.
		Time Complexity is O(n) because we need to visit each node in order to find
		the node to remove"""
		if self.is_empty():
			return "Linked List is empty. No nodes to remove."
		current = self.head
		previous = None
		found = False
		while not found:
			if current.get_data() == data:
				found = True
			elif current.get_next() == None:
				return "A node with that data value is not present"
			else:
				previous = current
				current = current.get_next()
		
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())