"""
Problem #13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""
# Input – Answer 1994
s = "MCMXCIV"

class Solution(object):
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		romans = {"I": 1, "V": 5, "X": 10, "L": 50,
					"C": 100, "D": 500, "M": 1000,
					"IV": 4, "IX": 9, "XL": 40,
					"XC": 90, "CD": 400, "CM": 900}
		
		# Determine which symbols can be added to the buffer in phrases
		i_phrase = ["V", "X"]
		x_phrase = ["L", "C"]
		c_phrase = ["D", "M"]
		
		total = 0
		buffer = ""
	
		for idx, char in enumerate(s):
			# Avoid "Index out of range" errors
			if idx < len(s) - 1:
				next = s[idx + 1]
				# Guard clause for special cases
				if (char == "I" and next in i_phrase) \
				 or (char == "X" and next in x_phrase) \
				 or (char == "C" and next in c_phrase):
						buffer += char
						continue
			
			buffer += char
			# When buffer isn't empty, add current buffer value to the total
			total += romans[buffer]
			# Reset buffer
			buffer = ""

		return total

if __name__ == '__main__':
	sol = Solution()
	ans = sol.romanToInt(s)
	print(ans)

"""
Solution Stats: Solution 1
Runtime: 40 ms, faster than 62.72% of Python online submissions.
Memory Usage: 13.4 MB, less than 88.87%% of Python online submissions.
"""