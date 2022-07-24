"""
Python Data Structures - A Game-Based Approach
Queue class
Robin Andrews - https://compucademy.net/
"""

from collections import deque

# Queue using the collections deque structure
class Queue_d:
	def __init__(self):
		self.items = deque()
	
	def is_empty(self):
		# empty deque returns False
		return not self.items
	
	def enqueue(self, item):
		self.items.append(item)
	
	def dequeue(self):
		return self.items.popleft()
	
	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[0]
	
	def __str__(self) -> str:
		return str(self.items)

# Queue using the list structure
class Queue_l:
	def __init__(self):
		self.items = []
	
	def is_empty(self):
		# empty deque returns False
		return not self.items
	
	def enqueue(self, item):
		self.items.append(item)
	
	def dequeue(self):
		return self.items.pop(0)
	
	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[0]
	
	def __str__(self) -> str:
		return str(self.items)

if __name__ == '__main__':
	pass