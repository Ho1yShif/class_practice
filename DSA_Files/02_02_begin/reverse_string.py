"""
Python Data Structures - A Game-Based Approach
Stack challenge
Robin Andrews - https://compucademy.net/
"""
# The hard way: with a stack
import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# My original solution
# for char in string:
# 	s.push(char)

# empty = s.isempty()

# while empty == False:
# 	reversed_string += s.pop()
# 	empty = s.isempty()

# print(reversed_string)

# Improved solution: Use isempty() directly
for char in string:
	s.push(char)

while not s.isempty():
	reversed_string += s.pop()

print(reversed_string)

# The easy wa: with indexing
print(f'check: {string[::-1]}')