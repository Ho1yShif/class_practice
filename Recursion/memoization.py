"""
Why memoization?
–It takes a long time to perform all the duplicate calculations required for conventional recursion
–Memoization can optimize code by storing computation results in a cache
–The function can retrieve stored values from the cache the next time they're needed,
instead of computing those same values again
(Source: https://www.freecodecamp.org/news/memoization-in-javascript-and-react/)

This script implements memoization in 2 ways:
–Automatically using the built-in LRU (least recently used) caching decorator
–Manually
"""

import time
from functools import lru_cache

# No caching; very slow
def fib(n):
    """
    Returns the n-th Fibonacci number.
    """
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


# Amazing caching to find large values in the fastest time
@lru_cache
def fib_lru(n):
    """
    Returns the n-th Fibonacci number.
    """
    if n == 0 or n == 1:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)

"""
Manual caching using a dictionary
Mediocre time– not as fast as the decorator but much faster than plain recursion!
"""

def fib_cache(n, cache=None):
	"""If no modifications were made to the cache, create a dict to store calculations"""
	if cache is None:
		cache = {}
	"""If the nth fibonacci term has already been computed, find its value in the cache dict"""
	if n in cache:
		return cache[n]
	"""If n is 0 or 1, return n because fib(0) = 0 and fib(1) = 1"""
	if n <= 1:
		return n
	"""Outside of the above scenarios, simply compute the nth term and add it to the cache"""
	result = fib_cache(n - 1, cache) + fib_cache(n - 2, cache)
	cache[n] = result
	return result

n = 900

# start = time.perf_counter()
# fib(n)
# end = time.perf_counter()
# print("Plain recursive version. Seconds taken: {:.7f}".format(end - start))
#
# start = time.perf_counter()
# fib_lru(n)
# end = time.perf_counter()
# print("lru cache version. Seconds taken: {:.7f}".format(end - start))
#
start = time.perf_counter()
fib_cache(n)
end = time.perf_counter()
print("Manual cache version. Seconds taken: {:.7f}".format(end - start))
