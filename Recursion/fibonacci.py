"""
My explanation:
The first 4 numbers in the Fibonacci series are 1, 1, 2, 3, 5 (where the first element has index 0)
For fibonacci(4), the math is 3 + 2 = 5
We need to wait until the n goes down to 1; then, the calculation begins

Winding Process as n approaches 1:
return fibonacci(3) + fibonacci(2)
return fibonacci(2) + fibonacci(1)

Hit the base case (n=1)!

Unwinding Process
return fibonacci(2) + fibonacci(1) = fibonacci(1) + fibonacci(0) + fibonacci(1) = 1 + 0 + 1 = 2
Knowing that fibonacci(2) = 2, we have:
return fibonacci(3) + fibonacci(2) = (fibonacci(2) + fibonacci(1)) + 2 = 2 + 1 + 1 = 5


Final value for fibonacci(4): 5
"""

def fibonacci(n):
	if n < 2:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(6))