"""
Problem #27. Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
# Input
nums = [0,1,2,2,3,0,4,2]
val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]

class Solution(object):
		def removeElement(self, nums, val) -> int:
			repl_idx = 0
			for idx, value in enumerate(nums):
				# Replace val with -1 since that's an impossible value for val
				if value == val:
					nums[idx] = -1
				# If not, replace the element at the earliest possible index
				else:
					nums[repl_idx] = value
					repl_idx = repl_idx + 1

			# The last repl_idx is the stopping post
			stop = repl_idx
			# Shorten nums to stop at the designated point
			nums = nums[:stop]
			return stop

if __name__ == '__main__':
	sol = Solution()
	ans = sol.removeElement(nums, val)
	print(ans)

"""
Solution Stats
Runtime: 24 ms, faster than 99.95% of Python online submissions for Isomorphic Strings.
Memory Usage: 14.2 MB, less than 87.75% of Python online submissions for Isomorphic Strings.
"""