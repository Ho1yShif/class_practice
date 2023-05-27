"""
Problem #724: Find Pivot Index
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
"""
# Input
nums = [-1,-1,0,0,-1,-1]

class Solution(object):
	def pivotIndex(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		length = len(nums)
		# Find the index of the next value in nums where the right sum matches the left, else return -1
		pivot_index = next((i for i in range(length) if (sum(nums[:i+1]) == sum(nums[i:]))), -1)
		
		return pivot_index

if __name__ == '__main__':
	sol = Solution()
	ans = sol.pivotIndex(nums)
	print(ans)

"""
Solution Stats
Runtime: 6428 ms, faster than 8.22% of Python online submissions for Find Pivot Index.
Memory Usage: 14.6 MB, less than 40.06% of Python online submissions for Find Pivot Index.
"""