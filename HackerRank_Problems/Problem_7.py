# ============================================================
# HackerRank Problem: Merge the Tools!
# ============================================================
#
# Problem Statement:
#
# You are given a string 'string' and an integer 'k'.
#
# The length of the string is divisible by k.
#
# You have to divide the string into k-sized groups.
#
# For each group:
#   1. Remove duplicate characters.
#   2. Keep only the first occurrence of each character.
#   3. Maintain the original order of the characters.
#   4. Print the resulting string.
#
# Example:
#
# Input:
# AABCAAADA
# 3
#
# Divide the string into groups of size 3:
#
# AAB
# CAA
# ADA
#
# Remove duplicate characters:
#
# AAB -> AB
# CAA -> CA
# ADA -> AD
#
# Output:
#
# AB
# CA
# AD
#
# ============================================================
# Solution Explanation:
# ============================================================
#
# We use range() to move through the string in steps of k.
#
# range(0, len(string), k)
#
# For example:
#
# string = "AABCAAADA"
# k = 3
#
# i values will be:
# 0, 3, 6
#
# We then use string slicing:
#
# group = string[i:i+k]
#
# This gives:
#
# i = 0  -> "AAB"
# i = 3  -> "CAA"
# i = 6  -> "ADA"
#
# For every group, we create an empty string called 'res'.
#
# Then we check every character:
#
# if char not in res:
#     res += char
#
# This ensures that a character is added only once.
#
# Finally, we print the result for each group.
#
# ============================================================


def merge_the_tools(string, k):

    # Move through the string in groups of size k
    for i in range(0, len(string), k):

        # Extract a group of k characters
        group = string[i:i+k]

        # Empty string to store unique characters
        res = ""

        # Check each character in the group
        for char in group:

            # Add the character only if it is not already present
            if char not in res:
                res += char

        # Print the unique characters
        print(res)


# ============================================================
# Taking Input
# ============================================================

if __name__ == '__main__':

    # Read the string
    string = input()

    # Read the value of k and convert it to integer
    k = int(input())

    # Call the function
    merge_the_tools(string, k)