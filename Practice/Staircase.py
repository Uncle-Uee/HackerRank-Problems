"""
Created by: Uee
Modified by:

Usage: Do what you want, Modify like you want.
"""

def staircase(n):
	for i in range(0,n):
		stairs = " " * (n - 1 - i)
		stairs += "#" * (i + 1)
		print(stairs)

# Example
staircase(4)
