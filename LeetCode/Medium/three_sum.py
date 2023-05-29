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
        # Account for 3-element case
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []

        nums.sort()
        output = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate values for i by checking left neighbor
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            # Nested two sum solution using two pointers
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    # Skip duplicate values for left using left neighbor
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for right using left neighbor
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1

        return output


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    sol = Solution()
    ans = sol.threeSum(nums)
    print(ans)

"""
Solution Stats
Runtime: 1633 ms, faster than 44.77% of Python online submissions
Memory Usage: 20.5 MB, less than 39.65% of Python online submissions
"""