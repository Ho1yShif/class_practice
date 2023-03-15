"""
Problem #58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
"""
# Input
s = "   fly me   to   the moon  "
# Output: 4

class Solution(object):
	def lengthOfLastWord_v1(self, s: str) -> int:
		# Split string on space and return length of last index
		last = s.split()[-1]
		return len(last)
	
	def lengthOfLastWord_v2(self, s: str) -> int:
		# Capture last word using regex
		import re
		substring = re.search('(\w+)\s*$', s).group(1)
		return len(substring)

if __name__ == '__main__':
	sol = Solution()
	ans = sol.searchInsert(nums, target)
	print(ans)

"""
Solution Stats: Solution V1
Runtime: 31 ms, faster than 67.90% of Python online submissions.
Memory Usage: 13.9 MB, less than 70.91% of Python online submissions.

Solution Stats: Solution V2
Runtime: 165 ms, faster than 5.16% of Python online submissions.
Memory Usage: 13.9 MB, less than 70.91% of Python online submissions.
"""