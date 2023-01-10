"""
Problem #205: Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""
# Input
s = "egg"
t = "add"

class Solution(object):
	def isIsomorphic(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		mapping_s_t = {}
		mapping_t_s = {}
		
		for s_char, t_char in zip(s, t):
			# If letters aren't mapped yet...
			if (not s_char in mapping_s_t) and (not t_char in mapping_t_s):
				mapping_s_t[s_char] = t_char
				mapping_t_s[t_char] = s_char
			
			# If one letter doesn't map to the corresponding letter in the other string
			elif mapping_s_t.get(s_char) != t_char or mapping_t_s.get(t_char) != s_char:
				return False
		
		return True

if __name__ == '__main__':
	sol = Solution()
	ans = sol.isIsomorphic(s, t)
	print(ans)

"""
Solution Stats
Runtime: 24 ms, faster than 99.95% of Python online submissions for Isomorphic Strings.
Memory Usage: 14.2 MB, less than 87.75% of Python online submissions for Isomorphic Strings.
"""