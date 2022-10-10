"""
My explanation:
Traverse a binary tree recursively

Preorder traversal: Root->Left->Right
Inorder traversal: Left->Root->Right
Postorder traversal: Left->Right->Root

Base case: there is no content at the root node

Until then, add nodes to the path in the order specified by the given traversal method.
Once there's no content left at the root, output the traversal path
"""
r"""
Tree shape:
		  ______F______
		 /             \
	  __D__           __I__
	 /     \         /     \
	B       E       G       J
   / \               \
  A   C               H
"""

class Node:
	def __init__(self, data) -> None:
		self.data = data
		self.left = None
		self.right = None

def preorder_print(root, path=""):
	"""Root->Left->Right"""
	if root:
		path += str(root.data) + "-"
		path = preorder_print(root.left, path)
		path = preorder_print(root.right, path)
	return path

def inorder_print(root, path=""):
	"""Left->Root->Right"""
	if root:
		path = inorder_print(root.left, path)
		path += str(root.data) + "-"
		path = inorder_print(root.right, path)
	return path

def postorder_print(root, path=""):
	"""Left->Right->Root"""
	if root:
		path = postorder_print(root.left, path)
		path = postorder_print(root.right, path)
		path += str(root.data) + "-"
	return path
	

if __name__ == '__main__':
	# Set up tree:
	root = Node("F")
	root.left = Node("D")
	root.left.left = Node("B")
	root.left.left.left = Node("A")
	root.left.left.right = Node("C")
	root.left.right = Node("E")
	root.right = Node("I")
	root.right.left = Node("G")
	root.right.left.right = Node("H")
	root.right.right = Node("J")

print("Preorder:", preorder_print(root))
print("Inorder:", inorder_print(root))
print("Postorder", postorder_print(root))