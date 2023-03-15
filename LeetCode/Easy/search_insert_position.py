"""
Problem #35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
# Input
nums = [1,3,5,6]
target = 5
# Output: 2

class Solution(object):
	def searchInsert(self, nums, target) -> int:
		if target in nums:
			return nums.index(target)

		# If target is greater than the last index, return the array length
		if target > nums[-1]:
			return len(nums)
		# If target is less than the first index, return 0
		if target < nums[0]:
			return 0
		# If the lower consecutive number to target is in the array, return that index + 1
		if (target - 1) in nums:
			return (nums.index(target - 1)) + 1
		# Otherwise, loop through until you find a value larger than target
		for idx, val in enumerate(nums):
			if val > target:
				return idx

if __name__ == '__main__':
	sol = Solution()
	ans = sol.searchInsert(nums, target)
	print(ans)

"""
Solution Stats: Solution 1
Runtime: 48 ms, faster than 82.23% of Python online submissions.
Memory Usage: 14.7 MB, less than 72.10% of Python online submissions.
"""