"""
Problem 21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

list1 = [1,2,4]
list2 = [1,3,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
     def mergeTwoLists(self, list1, list2) -> ListNode:
        # Create two pointers, one to keep track of loop and one to return later
        cur = dummy = ListNode()
        while list1 and list2:               
            # Add smallest list value to next node
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
        
        # When only one list is left, add the last node from that list
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

if __name__ == '__main__':
	sol = Solution()
	ans = sol.mergeTwoLists(list1, list2)
	print(ans)

"""
Solution Stats: Solution 1
Runtime: 37 ms, faster than 74.53% of Python online submissions.
Memory Usage: 13.8 MB, less than 67.27% of Python online submissions.
"""