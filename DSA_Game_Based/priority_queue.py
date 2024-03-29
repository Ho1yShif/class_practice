"""
Python Data Structures - A Game-Based Approach
Priority Queue Class based on heapq.
Robin Andrews - https://compucademy.net/
"""

import heapq

# Methods: init, is_empty, put, get, str
class PriorityQueue:
	def __init__(self):
		self.elements = []
	
	def __str__(self) -> str:
		return str(self.elements)
	
	def isempty(self):
		return not self.elements
	
	def put(self, item, priority):
		heapq.heappush(self.elements, (priority, item))
	
	def get(self):
		return heapq.heappop(self.elements)[1]

if __name__ == '__main__':
	pq = PriorityQueue()