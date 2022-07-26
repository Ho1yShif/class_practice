"""
My first stack
Shifra Isaacs
"""

class Stack:
	def __init__(self):
		self.items = []
	
	def __str__(self) -> str:
		return str(self.items)
	
	def isempty(self):
		return not self.items

	def push(self, item):
		self.items.append(item)
		return self.items

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	# New method
	def clear(self):
		check = input('Are you sure you want to clear the stack? (Y/N) ')
		if check.lower() == 'y':
			self.items = []