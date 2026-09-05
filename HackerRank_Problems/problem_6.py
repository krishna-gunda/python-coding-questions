'''
# ============================================================

# PYTHON REGEX (REGULAR EXPRESSIONS)

# ============================================================

#

# What is Regex?

# ------------------------------------------------------------

# Regex stands for "Regular Expression".

#

# A Regular Expression is a pattern used to search, find,

# match, extract, replace, or validate text.

#

# In simple words:

#

# Regex = A way to describe a pattern in text.

#

# Example:

#

# Text:

# "My phone number is 9876543210"

#

# We can use Regex to find the 10-digit phone number.

#

# ============================================================

# WHY DO WE USE REGEX?

# ============================================================

#

# Regex is useful when we want to work with text and search

# for specific patterns.

#

# Common uses:

#

# 1. Find numbers inside text

# 2. Find words inside text

# 3. Validate email addresses

# 4. Validate phone numbers

# 5. Validate passwords

# 6. Find URLs

# 7. Extract dates

# 8. Extract usernames

# 9. Replace specific text

# 10. Remove unwanted characters

# 11. Search for repeated patterns

# 12. Clean text before Machine Learning

# 13. Process large amounts of text

#

# ============================================================

# REAL-WORLD EXAMPLES

# ============================================================

#

# Example 1: Find a phone number

#

# Text:

# "Contact me at 9876543210"

#

# Regex:

# r"\d{10}"

#

# This searches for exactly 10 digits.

#

#

# Example 2: Find an email

#

# Text:

# "Contact: [example@gmail.com](mailto:example@gmail.com)"

#

# Regex can be used to identify the email address.

#

#

# Example 3: Find dates

#

# Text:

# "The meeting is on 05-09-2026"

#

# Regex can be used to find:

#

# 05-09-2026

#

# ============================================================

# REGEX IN PYTHON

# ============================================================

#

# Python provides the "re" module for Regular Expressions.

#

# First import the module:

#

# import re

#

# Example:

#

# import re

#

# text = "My age is 22"

#

# result = re.search(r"\d+", text)

#

# print(result.group())

#

# Output:

#

# 22

#

# ============================================================

# IMPORTANT REGEX FUNCTIONS

# ============================================================

#

# Python's re module provides several important functions.

#

# ------------------------------------------------------------

# 1. re.search()

# ------------------------------------------------------------

#

# Searches for the first occurrence of a pattern anywhere

# in the string.

#

# Example:

#

# import re

#

# text = "Python is easy"

#

# result = re.search("Python", text)

#

# print(result.group())

#

# Output:

# Python

#

#

# ------------------------------------------------------------

# 2. re.match()

# ------------------------------------------------------------

#

# Checks whether the pattern exists at the beginning

# of the string.

#

# Example:

#

# import re

#

# text = "Python is easy"

#

# result = re.match("Python", text)

#

# print(result.group())

#

# Output:

# Python

#

#

# ------------------------------------------------------------

# 3. re.findall()

# ------------------------------------------------------------

#

# Finds ALL matching patterns and returns them as a list.

#

# Example:

#

# import re

#

# text = "I have 10 apples and 20 oranges"

#

# numbers = re.findall(r"\d+", text)

#

# print(numbers)

#

# Output:

# ['10', '20']

#

#

# ------------------------------------------------------------

# 4. re.sub()

# ------------------------------------------------------------

#

# Used to replace matching text.

#

# Example:

#

# import re

#

# text = "I love Java"

#

# result = re.sub("Java", "Python", text)

#

# print(result)

#

# Output:

# I love Python

#

#

# ------------------------------------------------------------

# 5. re.split()

# ------------------------------------------------------------

#

# Splits a string using a Regex pattern.

#

# Example:

#

# import re

#

# text = "apple,banana orange"

#

# result = re.split(r"[, ]", text)

#

# print(result)

#

# Output:

# ['apple', 'banana', 'orange']

#

# ============================================================

# IMPORTANT REGEX SYMBOLS

# ============================================================

#

# Regex uses special characters to represent patterns.

#

# ------------------------------------------------------------

# 1. \d

# ------------------------------------------------------------

#

# Matches any digit from 0 to 9.

#

# Example:

#

# r"\d"

#

# Matches:

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

#

#

# ------------------------------------------------------------

# 2. \D

# ------------------------------------------------------------

#

# Matches anything that is NOT a digit.

#

# Example:

#

# r"\D"

#

#

# ------------------------------------------------------------

# 3. \w

# ------------------------------------------------------------

#

# Matches a word character.

#

# Usually includes:

#

# Letters

# Numbers

# Underscore (_)

#

# Example:

#

# r"\w+"

#

#

# ------------------------------------------------------------

# 4. \W

# ------------------------------------------------------------

#

# Matches anything that is NOT a word character.

#

#

# ------------------------------------------------------------

# 5. \s

# ------------------------------------------------------------

#

# Matches whitespace.

#

# Examples:

#

# Space

# Tab

# Newline

#

#

# ------------------------------------------------------------

# 6. \S

# ------------------------------------------------------------

#

# Matches anything that is NOT whitespace.

#

# ============================================================

# CHARACTER CLASSES

# ============================================================

#

# ------------------------------------------------------------

# [abc]

# ------------------------------------------------------------

#

# Matches one character that is either:

#

# a OR b OR c

#

# Example:

#

# r"[abc]"

#

#

# ------------------------------------------------------------

# [a-z]

# ------------------------------------------------------------

#

# Matches lowercase letters from a to z.

#

#

# ------------------------------------------------------------

# [A-Z]

# ------------------------------------------------------------

#

# Matches uppercase letters from A to Z.

#

#

# ------------------------------------------------------------

# [0-9]

# ------------------------------------------------------------

#

# Matches digits from 0 to 9.

#

#

# ------------------------------------------------------------

# [^abc]

# ------------------------------------------------------------

#

# Matches any character EXCEPT a, b, or c.

#

# ============================================================

# QUANTIFIERS

# ============================================================

#

# Quantifiers tell Regex how many times a pattern should occur.

#

# ------------------------------------------------------------

# *

# ------------------------------------------------------------

#

# Matches ZERO or MORE occurrences.

#

# Example:

#

# r"a*"

#

# Can match:

#

# ""

# "a"

# "aa"

# "aaa"

#

#

# ------------------------------------------------------------

# +

# ------------------------------------------------------------

#

# Matches ONE or MORE occurrences.

#

# Example:

#

# r"a+"

#

# Can match:

#

# "a"

# "aa"

# "aaa"

#

#

# ------------------------------------------------------------

# ?

# ------------------------------------------------------------

#

# Matches ZERO or ONE occurrence.

#

# Example:

#

# r"colou?r"

#

# Matches:

#

# color

# colour

#

#

# ------------------------------------------------------------

# {n}

# ------------------------------------------------------------

#

# Matches exactly n occurrences.

#

# Example:

#

# r"\d{10}"

#

# Matches exactly 10 digits.

#

#

# ------------------------------------------------------------

# {n,m}

# ------------------------------------------------------------

#

# Matches between n and m occurrences.

#

# Example:

#

# r"\d{2,4}"

#

# Can match:

#

# 12

# 123

# 1234

#

# ============================================================

# ANCHORS

# ============================================================

#

# Anchors specify the position of a pattern.

#

# ------------------------------------------------------------

# ^

# ------------------------------------------------------------

#

# Means START of the string.

#

# Example:

#

# r"^Hello"

#

# Matches:

#

# Hello World

#

# But not:

#

# Hi Hello

#

#

# ------------------------------------------------------------

# $

# ------------------------------------------------------------

#

# Means END of the string.

#

# Example:

#

# r"world$"

#

# Matches:

#

# Hello world

#

# ============================================================

# DOT (.)

# ============================================================

#

# "." matches almost any single character.

#

# Example:

#

# r"c.t"

#

# Can match:

#

# cat

# cut

# cot

# c9t

#

# ============================================================

# GROUPS

# ============================================================

#

# Parentheses () are used to create groups.

#

# Example:

#

# r"(cat|dog)"

#

# Matches either:

#

# cat

# OR

# dog

#

# ============================================================

# OR OPERATOR

# ============================================================

#

# "|" means OR.

#

# Example:

#

# r"cat|dog"

#

# Matches:

#

# cat

# dog

#

# ============================================================

# ESCAPING SPECIAL CHARACTERS

# ============================================================

#

# Some characters have special meanings in Regex.

#

# For example:

#

# .

# *

# +

# ?

# ^

# $

# (

# )

# [

# ]

#

# If we want to search for the actual character,

# we can use a backslash.

#

# Example:

#

# r"."

#

# This searches for an actual dot.

#

# ============================================================

# RAW STRINGS (r"")

# ============================================================

#

# In Python, Regex patterns are commonly written using

# raw strings.

#

# Example:

#

# r"\d+"

#

# instead of:

#

# "\d+"

#

# The "r" tells Python to treat backslashes as literal

# characters instead of processing them as normal escape

# sequences.

#

# ============================================================

# COMMON REGEX PATTERNS

# ============================================================

#

# ------------------------------------------------------------

# Find numbers

# ------------------------------------------------------------

#

# r"\d+"

#

#

# ------------------------------------------------------------

# Find exactly 10-digit phone numbers

# ------------------------------------------------------------

#

# r"\d{10}"

#

#

# ------------------------------------------------------------

# Find lowercase letters

# ------------------------------------------------------------

#

# r"[a-z]+"

#

#

# ------------------------------------------------------------

# Find uppercase letters

# ------------------------------------------------------------

#

# r"[A-Z]+"

#

#

# ------------------------------------------------------------

# Find only digits

# ------------------------------------------------------------

#

# r"^\d+$"

#

#

# ------------------------------------------------------------

# Find only letters

# ------------------------------------------------------------

#

# r"^[A-Za-z]+$"

#

#

# ------------------------------------------------------------

# Find letters and numbers

# ------------------------------------------------------------

#

# r"^[A-Za-z0-9]+$"

#

# ============================================================

# REGEX FOR DATA VALIDATION

# ============================================================

#

# Regex is commonly used to check whether user input follows

# a particular format.

#

# Examples:

#

# Email

# Phone number

# Password

# Username

# PIN code

# Date

# Website URL

#

# Example:

#

# import re

#

# phone = "9876543210"

#

# pattern = r"^\d{10}$"

#

# if re.match(pattern, phone):

# print("Valid phone number")

# else:

# print("Invalid phone number")

#

# ============================================================

# REGEX IN DATA SCIENCE AND AI

# ============================================================

#

# Regex is very useful in Data Science and AI, especially

# when working with text data.

#

# Common applications:

#

# 1. Text preprocessing

# 2. Data cleaning

# 3. Removing special characters

# 4. Extracting numbers

# 5. Extracting emails

# 6. Extracting URLs

# 7. Removing unwanted symbols

# 8. Finding patterns in text

# 9. Preparing text for NLP

# 10. Extracting useful information from raw data

#

# Example:

#

# Text:

#

# "The price is $500!!!"

#

# We can use Regex to remove special characters and

# keep only useful text.

#

# ============================================================

# REGEX IN WEB DEVELOPMENT

# ============================================================

#

# Regex can be used for:

#

# - Form validation

# - Email validation

# - Phone number validation

# - Username validation

# - Password format checking

# - Input validation

#

# Flask and FastAPI applications can use Regex to validate

# incoming user data.

#

# ============================================================

# REGEX IN LOG FILE ANALYSIS

# ============================================================

#

# Large applications generate log files.

#

# Regex can help find:

#

# - IP addresses

# - Error messages

# - Dates

# - Status codes

# - User IDs

# - URLs

#

# Example:

#

# Search all "ERROR" messages from a large log file.

#

# ============================================================

# REGEX IN NLP

# ============================================================

#

# NLP = Natural Language Processing

#

# Regex is often used as an initial text-processing technique.

#

# Examples:

#

# - Remove punctuation

# - Find words

# - Extract numbers

# - Extract hashtags

# - Extract mentions

# - Clean unwanted symbols

#

# ============================================================

# IMPORTANT THINGS TO REMEMBER

# ============================================================

#

# Regex is NOT a programming language.

#

# Regex is a pattern-matching technique.

#

# Python provides the "re" module to work with Regex.

#

# The most important functions are:

#

# re.search()

# re.match()

# re.findall()

# re.sub()

# re.split()

#

# The most important symbols are:

#

# \d      -> digit

# \D      -> not a digit

# \w      -> word character

# \W      -> not a word character

# \s      -> whitespace

# \S      -> not whitespace

# .       -> any character

# ^       -> beginning

# $       -> end

# *       -> zero or more

# +       -> one or more

# ?       -> zero or one

# {n}     -> exactly n

# {n,m}   -> between n and m

# []      -> character set

# ()      -> group

# |       -> OR

#

# ============================================================

# BEGINNER LEARNING ORDER

# ============================================================

#

# Learn Regex in this order:

#

# 1. Understand what Regex is

# 2. Learn the re module

# 3. Learn re.search()

# 4. Learn re.match()

# 5. Learn re.findall()

# 6. Learn re.sub()

# 7. Learn re.split()

# 8. Learn \d, \w, \s

# 9. Learn character classes []

# 10. Learn quantifiers *, +, ?, {n}, {n,m}

# 11. Learn ^ and $

# 12. Learn groups ()

# 13. Learn OR |

# 14. Learn Regex validation

# 15. Practice real-world text extraction

#

# ============================================================

# SIMPLE DEFINITION TO REMEMBER

# ============================================================

#

# Regex is a pattern-matching tool used to search, extract,

# validate, replace, and clean text.

#

# ============================================================
'''