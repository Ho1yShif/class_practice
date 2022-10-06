"""
My explanation:
For factorial(3), the math is 3 * 2 * 1
We need to wait until the argument to the function goes down to 1; then, the calculation begins

Winding Process as n approaches 1:
return 3 * factorial(2)
return 2 * factorial(1)
return 1 * factorial(0)

Hit the base case!

Unwinding Process
return 1 * factorial(0) = 1
return 2 * factorial(1) = 2
return 3 * factorial(2) = 6

Final value: 6
"""

def factorial(n):
	if n <= 1:
		# Base case
		return 1
	else:
		# Recursive case
		return n * factorial(n - 1)

print(factorial(4))
print(factorial(6))
print(factorial(1))
print(factorial(0))
print(factorial(-7))
# print(factorial(1000)) # RecursionError: maximum recursion depth exceeded in comparison