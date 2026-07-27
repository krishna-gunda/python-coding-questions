'''Assign Grades based on the marks'''


'''90-100 → A
80-89  → B
70-79  → C
60-69  → D
Below 60 → F'''


def grade(marks):
    if marks >=90:
        return "Grade A"
    elif marks>=80:
        return "Grade B"
    elif marks>=70:
        return "Grade c"
    elif marks>=60:
        return "Grade D"
    else:
        return "Fail"
    

print(grade(90))
print(grade(60))


