"""
Created by: Uee
Modified by:

Usage: Do what you want, Modify like you want.
"""

def timeConversion(s = ""):
	time24 = {"01": "13", "02": "14", "03": "15", "04": "16", "05": "17", "06": "18", "07": "19", "08": "20",
	          "09": "21", "10": "22", "11": "23", "12": "00"}
	hour = s[0: 2]
	period = s[-2: len(s)]

	if hour != "12" and period == "AM":
		return s[0: len(s) - 2]
	elif hour == "12" and period == "AM":
		return time24[hour] + s[2: len(s) - 2]
	elif hour != "12" and period == "PM":
		return time24[hour] + s[2: len(s) - 2]
	elif hour == "12" and period == "PM":
		return s[0: len(s) - 2]

# Example
timeConversion("11:15:15PM")
