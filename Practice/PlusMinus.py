"""
Created by: Uee
Modified by:

Usage: Do what you want, Modify like you want.
"""

def plusMinus(arr):
	n = len(arr)

	print(round(len([i for i in arr if i > 0]) / n, 6))
	print(round(len([i for i in arr if i < 0]) / n, 6))
	print(round(len([i for i in arr if i == 0]) / n, 6))
