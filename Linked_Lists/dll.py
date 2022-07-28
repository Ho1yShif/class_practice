class DLLNode:

	def __init__(self, data):
		self.data = data
		self.next = None
		self.previous = None

	def __repr__(self):
		return "DLLNode object: data={}".format(self.data)

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
	
	def get_previous(self):
		return self.previous
		
	def set_previous(self, new_previous):
		self.previous = new_previous

class DLL:
	def __init__(self):
		self.head = None
	
	def __repr__(self) -> str:
		return "<DLL object: head={}>".format(self.head)
	
	def is_empty(self):
		return not self.head

	def size(self):
		"""Traverses the DLL and returns an int value representing the number of nodes
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

	def add_front(self, new_data):
		"""Add a Node whose data is the new_data argument to the front of the DLL"""
		temp = DLLNode(new_data)
		temp.set_next(self.head)

		# If LL is not empty, set previous head pointer to new node
		if self.head is not None:
			self.head.set_previous(temp)
		
		self.head = temp

	def remove(self, data):
		"""Removes the first occurrence of a Node that contains the data argument as its self.data attribute. Returns nothing.
		Time complexity is O(n) because in the worst case, we must visit every node before finding the one we want to remove"""
		if self.is_empty():
			return "Linked List is empty. No nodes to remove."
		
		current = self.head
		found = False
		while not found:
			# Case: we find the data in a Node
			if current.get_data() == data:
				found = True
			# Case: we reach the end of the linked list without finding data
			elif current.get_next() is None:
					return "A node with that data value is not present"
			# Otherwise, continue traversing
			else:
				current = current.get_next()
		
		# We reach here if we FIND the data we're looking for
		# Case: Data is first node; remove first node
		if current.previous is None:
			self.head = current.get_next()
		# Case: Data is a middle node. Replace the pointers pointing to this node in both directions, so it's effectively removed
		else:
			current.previous.set_next(current.get_next()) # Previous node will now point to next node
			current.next.set_previous(current.get_previous()) # Next node will now point to previous node