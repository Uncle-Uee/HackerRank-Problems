"""
Created by: Uee
Modified by:

Usage: Do what you want, Modify like you want.
"""

def compareTriplets(a, b):
	comparison = [0, 0]

	for i in range(len(a)):
		comparison[0] += 1 if a[i] > b[i] else 0
		comparison[1] += 1 if b[i] > a[i] else 0

	return comparison

# Example
print(compareTriplets([17, 28, 30], [99, 16, 8]))
