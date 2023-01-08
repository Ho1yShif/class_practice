"""
Problem #217: Contains Duplicate
Given an integer array nums, return true if any value appears at least
twice in the array, and return false if every element is distinct.
"""
# Input
nums = [1,2,3,1]

class Solution1(object):
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if len(nums) == len(set(nums)):
			return False
		
		return True

class Solution2(object):
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		unique_nums = set()
		for num in nums:
			if num in unique_nums:
				return True
			unique_nums.add(num)
		return False

if __name__ == '__main__':
	sol = Solution1()
	ans = sol.containsDuplicate(nums)
	print(ans)

"""
Solution Stats: Solution 1
Runtime: 385 ms, faster than 92.90% of Python online submissions for Contains Duplicate.
Memory Usage: 23.9 MB, less than 41.58% of Python online submissions for Contains Duplicate.

Solution Stats: Solution 2
Runtime: 427 ms, faster than 99.83% of Python online submissions for Contains Duplicate.
Memory Usage: 26 MB, less than 28.10% of Python online submissions for Contains Duplicate.
"""