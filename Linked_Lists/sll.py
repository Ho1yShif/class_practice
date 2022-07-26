from dataclasses import dataclass

# Singly Linked List Node Object
class SLLNode:

	def __init__(self, data):
		self.data = data
		self.next = None
	
	def __repr__(self) -> str:
		return "SLL Node Object: data={}".format(self.data)

	def get_data(self):
		return self.data
	
	def set_data(self, new_data):
		self.data = new_data
	
	def get_next(self):
		return self.next
	
	def set_next(self, new_next):
		self.next = new_next

if __name__ == '__main__':
	node = SLLNode('Shif')
	node2 = SLLNode('Zack')
	node.set_next(node2)
	node.get_next()