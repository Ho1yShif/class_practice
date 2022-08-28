"""
Problem #217: Contains Duplicate
Given an integer array nums, return true if any value appears at least
twice in the array, and return false if every element is distinct.
"""
# Input
nums = [1,2,3,1]

class Solution(object):
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if len(nums) == len(set(nums)):
			return False
		
		return True

if __name__ == '__main__':
	sol = Solution()
	ans = sol.containsDuplicate(nums)
	print(ans)

"""
Solution Stats
Runtime: 385 ms, faster than 92.90% of Python online submissions for Contains Duplicate.
Memory Usage: 23.9 MB, less than 41.58% of Python online submissions for Contains Duplicate.
"""