'''🎯 Random Python Problem #1 — Student Performance Analyzer

Create a Python program that analyzes the marks of students.

Problem

You are given a dictionary containing student names and their marks in 3 subjects:

students = {
    "Rahul": [78, 85, 92],
    "Priya": [90, 88, 95],
    "Arjun": [45, 67, 55],
    "Sneha": [32, 40, 38],
    "Kiran": [76, 72, 80]
}

Your program should:

Calculate the total marks of every student.
Calculate the average marks of every student.
Determine the student's grade:
Average >= 90 → A
Average >= 75 → B
Average >= 60 → C
Average >= 40 → D
Average < 40 → F
Find the student with the highest average.
Find all students who failed.
Display the results in this format:
Rahul -> Total: 255, Average: 85.0, Grade: B
Priya -> Total: 273, Average: 91.0, Grade: A
Arjun -> Total: 167, Average: 55.67, Grade: D
Sneha -> Total: 110, Average: 36.67, Grade: F
Kiran -> Total: 228, Average: 76.0, Grade: B

Top Student: Priya
Failed Students: Sneha
Rules

Try to solve it using:

for loop
if/elif/else
dictionary
list
sum()
len()
variables'''

