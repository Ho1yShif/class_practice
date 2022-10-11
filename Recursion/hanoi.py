"""
Towers of Hanoi Game
Application of recursion
Online version: https://www.mathsisfun.com/games/towerofhanoi.html
"""

def towers_of_hanoi(n, source, destination, auxiliary):
	"""If we only have one ring (base case), just move it from source to destination"""
	if n == 1:
		print(f"Move disk 1 from source {source} to {destination}")
		return
	"""If we have more than one ring, solve for n-1 discs
	Here, the auxiliary (spare) ring becomes the destination"""
	towers_of_hanoi(n - 1, source, auxiliary, destination)
	print(f"Move disk {n} from source {source} to destination {destination}")
	"""Move the base then solve it for n-1 discs again
	Here, the auxiliary (spare) ring becomes the source"""
	towers_of_hanoi(n - 1, auxiliary, destination, source)


n = 4
# A, C, B are the names of the rods.
# They correspond to source, destination, auxiliary
towers_of_hanoi(n, 'A', 'C', 'B')