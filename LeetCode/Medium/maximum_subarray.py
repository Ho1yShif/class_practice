"""
Problem #53: Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""

nums = [-2,1,-3,4,-1,2,1,-5,4]

class Solution(object):
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize the max sum below the smallest possible number and the current sum at 0
        max_sum = -10**5
        curr_sum = 0

        for num in nums:
            # Compare running sum to current element to ensure that the running sum is always the max sum of a subarray that ends at the current element
            curr_sum = max(curr_sum + num, num)
            # Reset max sum if curr_sum is greater
            max_sum = max(max_sum, curr_sum)
        return max_sum


if __name__ == '__main__':
	sol = Solution()
	ans = sol.maxSubArray(nums)
	print(ans)

"""
Solution Stats
Runtime: 753 ms, faster than 86.75% of Python online submissions for Contains Duplicate.
Memory Usage: 28.6 MB, less than 85.19% of Python online submissions for Contains Duplicate.
"""