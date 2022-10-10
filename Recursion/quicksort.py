"""
My explanation:
The numbers in [5, 2, 6, 3, 1] should be sorted in the order [1, 2, 3, 5, 6]
We need to wait until the sub-arrays contain 1 number or they're empty

Winding Process as length approaches 1:
For the overall list, pivot = arr[3] = 3
return quicksort([2, 1]) + [3] + quicksort([5, 6])

For quicksort([2, 1]), the pivot = arr[1] = 2
return quicksort([1]) + [2] + quicksort([])
We've reached the base case in this sub-function
Unwinding process
quicksort([2, 1]) returns [1, 2]

For quicksort([5, 6]), the pivot = arr[1] = 6
return quicksort([5]) + [6] + quicksort([])
We've reached the base case in this sub-function
Unwinding process
quicksort([5, 6]) returns [5, 6]

Final return: quicksort([2, 1]) + [3] + quicksort([5, 6]) = [1, 2] + [3] + [5, 6] = [1, 2, 3, 5, 6]
"""

def quicksort(arr):
	length = len(arr)
	if length <= 1:
		return arr
	pivot = arr[length // 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quicksort(left) + middle + quicksort(right)

def quicksort_verbose(arr):
	print(f"Calling quicksort on {arr}")
	if len(arr) <= 1:
		print(f"returning {arr}")
		return arr
	pivot = arr[len(arr) // 2]
	left = [x for x in arr if x < pivot]
	print(f"left: {left}; ", end="")
	middle = [x for x in arr if x == pivot]
	print(f"middle: {middle}; ", end="")
	right = [x for x in arr if x > pivot]
	print(f"right: {right}")
	to_return = quicksort_verbose(left) + middle + quicksort_verbose(right)
	print(f"returning: {to_return}")
	return to_return


# data = [5, 2, 6, 1]
# print(quicksort(data))
# print(quicksort_verbose(data))

# quicksort = trace(quicksort)
# quicksort(data)

# What about data with duplicates?
data = [1, 6, 5, 5, 2, 6, 1]
print(quicksort(data))