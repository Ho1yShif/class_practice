"""
Problem #9: Palindrome Number
Given an integer x, return true if x is a 
palindrome, and false otherwise.

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

class Solution(object):
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		x = str(x)
		return x == x[::-1]


if __name__ == '__main__':
	sol = Solution()
	ans = sol.isPalindrome(121)
	print(ans)

"""
Solution Stats
Runtime: 31 ms, faster than 99.76% of Python online submissions
Memory Usage: 13.5 MB, less than 15.61% of Python online submissions
"""