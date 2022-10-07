"""
My explanation:
2^3 = 8

Winding Process as n approaches 1
exp(2, 3)
return 2 * exp(2, 2)
return 2 * exp(2, 1)

Hit the base case (n == 1; a^1 = a)!

Unwinding Process
return 2 * exp(2, 1) = return 2 * 2 = return 4
return 8

Final value for exp(2, 3): 8
"""

def exp(a, n):
	if n == 1:
		return a
	else:
		return a * exp(a, n - 1)

assert exp(5, 3) == 125
assert exp(2, 4) == 16
assert exp(1, 19) == 1
assert exp(0, 2) == 0