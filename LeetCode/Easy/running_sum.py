"""
Problem #1480: Running Sum of 1d Array
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""

# Input
nums = [1, 2, 3, 4]

class Solution(object):
	def runningSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		length = len(nums)
		comp = [sum(nums[:i+1]) for i in range(length)]
		return comp

"""
Solution Stats
Runtime: 44 ms, faster than 39.06% of Python online submissions for Running Sum of 1d Array.
Memory Usage: 13.5 MB, less than 85.84% of Python online submissions for Running Sum of 1d Array.
"""