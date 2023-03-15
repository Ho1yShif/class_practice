"""
Problem #66. Plus One
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""
# Input
digits = [9]
# Output: [1,0]

class Solution(object):
	def plusOne(self, digits) -> list[int]:
		digits = [str(digit) for digit in digits]
		# Join digits, convert to int and increment, then convert back to string
		incremented = str(int(''.join(digits)) + 1)
		# Create output list of integers
		return [int(digit) for digit in incremented]

if __name__ == '__main__':
	sol = Solution()
	ans = sol.plusOne(digits)
	print(ans)

"""
Solution Stats
Runtime: 34 ms, faster than 65.5% of Python online submissions.
Memory Usage: 13.8 MB, less than 94.44% of Python online submissions.
"""