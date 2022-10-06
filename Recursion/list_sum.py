"""
My explanation:
The numbers in [1, 2, 4] add to 7
We need to wait until the list is empty (has length == 0); then, the calculation begins

Winding Process as n approaches 1:
return 1 + [2, 4]
return 2 + [4]
return 4 + []

Hit the base case (empty list)!

Unwinding Process
return 4 + [] = 4
return 2 + [4] = 6
return 1 + [2, 4] = 7

Final value for list_sum([1, 2, 4]): 7
"""

def list_sum(a_list):
	if len(a_list) == 0:
		return 0
	else:
		return a_list[0] + list_sum(a_list[1:])

assert list_sum([2, 3, 5, 7]) == 17
assert list_sum([-4, -3, -2, -1, 10]) == 0
assert list_sum([]) == 0
assert list_sum([3]) == 3
assert list_sum([-5, -3]) == -8