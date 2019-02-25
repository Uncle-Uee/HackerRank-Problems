"""
Created by: Uee
Modified by:

Usage: Do what you want, Modify like you want.
"""

def diagonalDifference(arr):
	primary = 0
	secondary = 0

	for i in range(0, len(arr)):
		primary += arr[i][i]
		secondary += arr[i][len(arr[i]) - 1 - i]

	return abs(primary - secondary)
