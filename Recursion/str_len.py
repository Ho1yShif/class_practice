"""
My explanation:
The length of "help" is 4
We need to wait until the string is empty (has length == 0); then, the calculation begins

Winding Process as n approaches 1:
str_len("help")
return str_len("elp") + 1
return str_len("lp") + 1
return str_len("p") + 1
return str_len("") + 1

Hit the base case (empty string)!

Unwinding Process
return str_len("") + 1 = 1
return str_len("p") + 1 = (1) + 1
return str_len("lp") + 1 = (2) + 1
return str_len("elp") + 1 = (3) + 1 = 4

Final value for str_len("help") = 4
"""

def str_len(a_str):
	if a_str == "":
		return 0
	else:
		return str_len(a_str[1:]) + 1

input_str = "I love recursion"
print(len(input_str))  # Standard Pythonic way
print(str_len(input_str))
print(str_len(input_str))
