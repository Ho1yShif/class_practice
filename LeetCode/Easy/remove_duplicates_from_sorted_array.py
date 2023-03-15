"""
Problem #26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		# Obtain a sorted set from nums along with its length
		unique = sorted(list(set(nums)))
		replace_idx = len(unique)

		# Replace the first values in nums with the sorted set
		nums[:replace_idx] = unique
		return replace_idx

if __name__ == '__main__':
	sol = Solution()
	ans = sol.removeDuplicates(nums)
	print(ans)

"""
Solution Stats: Solution 1
Runtime: 85 ms, faster than 83% of Python online submissions.
Memory Usage: 15.5 MB, less than 94.75% of Python online submissions.
"""