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
		if target not in nums:
			if target > nums[-1]:
				return len(nums)
			if target < nums[0]:
				return 0
			if (target - 1) in nums:
				return (nums.index(target - 1)) + 1
			for idx, val in enumerate(nums):
				if val > target:
					return idx

		else:
			return nums.index(target)

if __name__ == '__main__':
	sol = Solution()
	ans = sol.searchInsert(nums, target)
	print(ans)

"""
Solution Stats: Solution 1
Runtime: 48 ms, faster than 82.23% of Python online submissions.
Memory Usage: 14.7 MB, less than 72.10% of Python online submissions.
"""