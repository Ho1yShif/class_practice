"""
My explanation:
Traverse a [singularly] linked list recursively
Start at the head node and move through the "next" pointers until you reach the tail node

Base case: if the head is None, return None

Until then, print the node's data and move to the next node by calling the traversal function again
"""

class LL_Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

def traverse_LL(head):
	if head is None:
		return None
	print(head.data)
	traverse_LL(head.next)

item1 = LL_Node("first")
item2 = LL_Node("second")
item3 = LL_Node("third")
item1.next = item2
item2.next = item3

traverse_LL(item1)

# head = LL_Node("dog", LL_Node("cat", LL_Node("rat", None)))
# traverse_LL(head)