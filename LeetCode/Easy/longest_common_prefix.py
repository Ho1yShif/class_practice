"""
Problem #14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
# Input
strs = ["flower","flow","flight"]

class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		# Sort list
		strs.sort()

		# Store first and last words
		first = strs[0]
		last = strs[-1]
		
		"""Idx will represent how many characters are
		shared between first and last"""
		idx = 0
		while (idx < len(first)) and (idx < len(last)):
			if first[idx] == last[idx]:
				idx += 1
			else:
				break
		
		# Return substring of first word up to matching index
		return first[:idx]

if __name__ == '__main__':
	sol = Solution()
	ans = sol.longestCommonPrefix(strs)
	print(ans)

"""
Solution Stats: Solution 1
Runtime: 20 ms, faster than 71.44% of Python online submissions.
Memory Usage: 13.5 MB, less than 88.97%% of Python online submissions.
"""