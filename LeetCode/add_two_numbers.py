"""
Problem #2: Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
""" Input
l1 = [2,4,3]
l2 = [5,6,4]
Explanation: 342 + 465 = 807"""

# Problem's definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

	# Calculate the reversed number based on the digit's place in our linked list
		def combine_to_reverse_num(list_name):
			out = list_name.val
			start = list_name.next
			place = 10
			node = start
			while node:
				out += node.val * place
				node = node.next
				place *= 10
			return out
		
		# add 2 numbers as calculated from the lists
		target = combine_to_reverse_num(l1) + combine_to_reverse_num(l2)

		# Decompose target number into its digits using mathematical operations which are faster than string conversion
		digits_list = []
		while target >= 10:
			digits_list.append(target % 10)
			target //= 10
		digits_list.append(target)
		
		# Create output linked list using digits
		ll = ListNode(val=digits_list[0])
		curr_node = ll
		for digit in digits_list[1:]:
			next_node = ListNode(val=digit)
			curr_node.next = next_node
			curr_node = next_node
		
		return ll

# Can't run this code because we don't have the Linked List's structure

"""
Solution Stats
Runtime: 71 ms, faster than 82.45% of Python online submissions for Contains Duplicate.
Memory Usage: 13.8 MB, less than 85.19% of Python online submissions for Contains Duplicate.
"""