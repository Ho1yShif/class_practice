"""
Problem #500: Find Keyboard Row
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard.

In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
"""
# Input
words = ["Hello","Alaska","Dad","Peace"]

class Solution:
	def findWords(self, words: List[str]) -> List[str]:
		rows = {1: "qwertyuiop", 2: "asdfghjkl", 3: "zxcvbnm"}
		output = []
		
		for idx, word in enumerate(words):
			is_single_row = True
			which_row = 0
			word = word.lower()
			
			"""For 1-letter words, append to output and move onto next word"""
			if len(word) == 1:
				output.append(words[idx])
				continue
			
			"""Assign which_row variable so we know which row to match chars against"""
			if word[0] in rows[1]:
				which_row = 1
			elif word[0] in rows[2]:
				which_row = 2
			elif word[0] in rows[3]:
				which_row = 3
			
			"""Check each subsequent character against the specified keyboard row"""
			for char in word[1:]:
				if char not in rows[which_row]:
					is_single_row = False
					break
			
			if is_single_row == True:
				output.append(words[idx])
		
		return output

"""
Solution Stats
Runtime: 62 ms, faster than 26.15% of Python3 online submissions for Keyboard Row.
Memory Usage: 13.9 MB, less than 68.76% of Python3 online submissions for Keyboard Row.
"""