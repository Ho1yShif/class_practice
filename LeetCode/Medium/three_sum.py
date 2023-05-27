"""
Problem #15: 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
Constraints:

3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5"""

from typing import List

class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		# First account for 3-element case
		if len(nums) == 3:
			# Guard clause to check equality to 0
			if sum(nums) != 0:
				return []
			else:
				return [nums]

		output = []
		sorted_nums = sorted(nums)
		# Iterate until third-to-last element
		for i, num in enumerate(sorted_nums[:-2]):
			# Skip duplicates
			if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
				continue

			left = i + 1
			right = len(sorted_nums) - 1

			while left < right:
				check_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

				if check_sum == 0:
					triplet = [sorted_nums[i], sorted_nums[left], sorted_nums[right]]
					output.append(triplet)
					left += 1
					right -= 1

					# Skip duplicates
					while left < right and sorted_nums[left] == sorted_nums[left - 1]:
						left += 1

					# Skip duplicates
					while left < right and sorted_nums[right] == sorted_nums[right + 1]:
						right -= 1

				elif check_sum < 0:
					left += 1
				else:
					right -= 1

		return output

if __name__ == '__main__':
	nums = [-1,0,1,2,-1,-4]
	sol = Solution()
	ans = sol.threeSum(nums)
	print(ans)

"""
Solution Stats
Runtime: 1536 ms, faster than 50.26%% of Python online submissions
Memory Usage: 20.5 MB, less than 36.74%% of Python online submissions
"""