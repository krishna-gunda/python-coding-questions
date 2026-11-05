"""
HackerRank Problem: Finding the Day

Task:

You are given a date. Your task is to find what the day is on that date.

Input Format:

A single line of input containing the space-separated month, day, and year, respectively.

Output Format:

Output the correct day in CAPITAL LETTERS.

Sample Input:

08 05 2015

Sample Output:

WEDNESDAY

Explanation:

The day on August 5, 2015, was WEDNESDAY.
"""

import calendar

# Take month, day, and year as input
month, day, year = input().split(" ")

# Find the weekday number using calendar.weekday()
day_num = calendar.weekday(int(year), int(month), int(day))

# Convert the weekday number into its name
# Convert the day name into uppercase letters
print(calendar.day_name[day_num].upper())