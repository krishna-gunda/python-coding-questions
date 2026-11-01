"""
Problem: Minion Game

Kevin and Stuart play a game using a given string.

Rules:
1. Stuart gets points for substrings starting with consonants.
2. Kevin gets points for substrings starting with vowels (A, E, I, O, U).
3. Each substring occurrence gives one point.
4. The player with the highest score wins.
5. If both scores are equal, print Draw.

Example:
Input:
BANANA

Output:
Stuart 12
"""


def minion_game(string):
    # Initialize the scores of both players
    stuart = 0
    kevin = 0

    # Store the vowels in uppercase
    vowels = "AEIOU"

    # Visit every character in the string
    for i in range(len(string)):

        # Calculate how many substrings start at index i
        # Example: BANANA has 6 characters
        # At index 0, 6 substrings start with B
        # At index 1, 5 substrings start with A
        score = len(string) - i

        # If the character is a vowel, Kevin gets the points
        if string[i] in vowels:
            kevin += score

        # Otherwise, Stuart gets the points
        else:
            stuart += score

    # Compare the scores and print the winner
    if stuart > kevin:
        print("Stuart", stuart)

    elif kevin > stuart:
        print("Kevin", kevin)

    else:
        print("Draw")


if __name__ == '__main__':
    # Get the input string from the user
    s = input().strip()

    # Call the function to calculate the scores
    minion_game(s)