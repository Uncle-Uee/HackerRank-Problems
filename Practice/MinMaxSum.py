"""
Created by: Uee
Modified by:

Usage: Do what you want, Modify like you want.
"""

def miniMaxSum(arr):
	arr.sort()
	min = 0
	max = 0
	for i in range(0, len(arr) - 1):
		min += arr[i]
		max += arr[i + 1]

	print(str(min) + " " + str(max))

# Example
miniMaxSum([1, 3, 5, 7, 9])
