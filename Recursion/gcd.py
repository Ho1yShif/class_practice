"""
My explanation:
The GCD (Greates Common Divisor) of 16 and 12 is 4
This is different from GCF!

Winding Process as b approaches 0
gcd(16, 12)
gcd(12, 16 % 12) = gcd(12, 4)
gcd(4, 12 % 4) = gcd(4, 0)

Hit the base case (b == 0; no remainder)!

Unwinding Process
return 4

Final value for gcd(16, 12): 4

Note that a smaller # % a larger % just returns the larger number
"""

def gcd(a, b):
	if b == 0:
		# Base case
		return a
	else:
		# Recursive case
		return gcd(b, a % b)


print(gcd(16, 12))
print(gcd(50, 15))
print(gcd(42, 28))
print(gcd(28, 42))
print(gcd(345, 766))  # Co-prime