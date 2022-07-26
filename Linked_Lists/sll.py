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
		pass

	def size(self):
		pass

	def search(self, data):
		pass

	def remove(self, data):
		pass
		


if __name__ == '__main__':
	print(bool(None))