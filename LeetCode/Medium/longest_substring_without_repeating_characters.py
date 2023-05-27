"""
Problem #3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 10^4"""

from typing import List

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		length = len(s)
		used_chars = set()
		curr_len = 0
		max_len = 0
		start_idx = 0

		for idx, char in enumerate(s):
			if char in used_chars:
				while s[start_idx] != char:
					used_chars.remove(s[start_idx])
					start_idx += 1
				start_idx += 1

			used_chars.add(char)
			curr_len = idx - start_idx + 1
			max_len = max(max_len, curr_len)

		return max_len

if __name__ == '__main__':
	s = "abcabcbb"
	sol = Solution()
	ans = sol.lengthOfLongestSubstring(s)
	print(ans)

"""
Solution Stats
Runtime: 74 ms, faster than 54.52%% of Python online submissions
Memory Usage: 16.4 MB, less than 17.70%% of Python online submissions
"""