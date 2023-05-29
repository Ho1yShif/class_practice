"""
Problem #1: Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

nums = [2,7,11,15]

class Solution(object):
	def TwoSum(self, nums: list[int], target: int) -> list[int]:
		for outer_idx, outer_num in enumerate(nums):
			start = outer_idx
			remaining = target - nums[start]
			
			for nested_idx, nested_num in enumerate(nums[(outer_idx+1):]):
				if nested_num == remaining:
					# idx of nested loop + start outer idx + 1 from enumerate
					end = nested_idx + outer_idx + 1
					return [start, end]

if __name__ == '__main__':
	sol = Solution()
	ans = sol.TwoSum(nums, 9)
	print(ans)

"""
TwoSumBruteForce Solution Stats
Runtime: 2311 ms, faster than 27.48% of Python online submissions
Memory Usage: 14.9 MB, less than 76.30% of Python online submissions
"""