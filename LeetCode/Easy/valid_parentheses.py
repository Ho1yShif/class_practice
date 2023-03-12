"""
Problem 20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = 
Output: true
"""
s = "()[]{}"

class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
	
		stack = []
		closeToOpen = { ")":"(", "]":"[", "}":"{"}

		# Guard clause: return false if first char is a closing
		if s[0] in closeToOpen.keys():
			return False

		for char in s:
			if char in closeToOpen.keys():
				# If stack isn't empty and the last item is the matching opening bracket
				if stack and stack[-1] == closeToOpen[char]:
					stack.pop()
				else:
					return False
			# If it's an opening, append to stack
			else:
				stack.append(char)
		
		# Return true only if stack is empty
		return True if not stack else False

if __name__ == '__main__':
	sol = Solution()
	ans = sol.isValid(s)
	print(ans)

"""
Solution Stats: Solution 1
Runtime: 12 ms, faster than 92.63% of Python online submissions.
Memory Usage: 13.7 MB, less than 14.73% of Python online submissions.
"""