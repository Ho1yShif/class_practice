"""
Problem #392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 
Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

"""
# Input
s = "abc"
t = "ahbgdc"

class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		i = 0  # Pointer for string s
		j = 0  # Pointer for string t

		while i < len(s) and j < len(t):
			if s[i] == t[j]:
				i += 1  # Move pointer for string s
			j += 1  # Move pointer for string t

		return i == len(s)


if __name__ == '__main__':
	sol = Solution()
	ans = sol.isSubsequence(s, t)
	print(ans)

"""
Solution Stats
Runtime: 46 ms, faster than 39.48% of Python online submissions.
Memory Usage: 16.3 MB, less than 30.11% of Python online submissions.
"""