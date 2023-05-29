"""
Problem #167: Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""

nums = [2,7,11,15]

class Solution(object):
	def TwoSumTwoPointer(self, nums: list[int], target: int) -> list[int]:
		nums = sorted(nums)
		left = 0
		right = len(nums) - 1
		while left < right:
			# Account for one-indexing
			current_sum = nums[left + 1] + nums[right + 1]	
			if current_sum == target:
				return [left, right]
			elif current_sum < target:
				left += 1
			elif current_sum > target:
				right -= 1
			# Otherwise return empty list
		else:
			return []

if __name__ == '__main__':
	sol = Solution()
	ans = sol.TwoSumTwoPointer(nums, 9)
	print(ans)

"""
TwoSumTwoPointer Solution Stats
Runtime: 145 ms, faster than 25.48% of Python online submissions
Memory Usage: 17.3 MB, less than 31.90% of Python online submissions
"""