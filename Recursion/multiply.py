"""
My explanation:
5 * 3 = 15

Winding Process as n approaches 1
multiply(3, 5)
return 5 + multiply(2, 5)
return 5 + multiply(1, 5)

Hit the base case (n == 1; 1 * the number a)!

Unwinding Process
return 5
return 5 + (5) = 10
return 5 + (5 + 5) = 15

Final value for multiply(3, 5): 15
"""

def multiply(n, a):
	# Base case
	if n == 1:
		return a
	else:
		return a + multiply(n-1, a)


assert multiply(5, 4) == 20  # 5 is the multiplier, 4 is the multiplicand
assert multiply(5, -4) == -20  # 5 is the multiplier, -4 is the multiplicand
assert multiply(1, 4) == 4  # 1 is the multiplier, 4 is the multiplicand
assert multiply(7, 8) == 56  # 7 is the multiplier, 8 is the multiplicand

print(multiply(3, 5))