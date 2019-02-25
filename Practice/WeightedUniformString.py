"""
Created by: Shu'aib and Uee
Modified by:

Usage: Do what you want, Modify like you want.
"""

def weightedUniformString(s, queries):
	previous_letter = s[0]
	weight = ord(previous_letter) - 96
	weights = [weight]
	answers = []

	for next_letter in s[1:]:
		if previous_letter == next_letter:
			weight += ord(previous_letter) - 96
			weights.append(weight)
		else:
			weights.append(ord(next_letter) - 96)
			previous_letter = next_letter
			weight = ord(previous_letter) - 96

	for query in queries:
		answers.append("Yes") if query in weights else answers.append("No")

	return answers

# Example
print(weightedUniformString("abccddde", [1, 3, 12, 5, 9, 10]))
