'''Student Marks — Validate Private Data

Create a Student class with a private variable __marks.

Create methods:

set_marks(marks)
get_marks()

Rules:

Marks must be between 0 and 100.
If marks are outside this range, print "Invalid marks".'''



class Student_Marks:
    def __init__(self,marks):
        if marks>=0 and marks<=100:
            self.__marks=marks
        else:
            print("Marks Invalid")    
    def set_marks(self,marks):
        if marks>=0 and marks<=100:
            self.__marks=marks
        else:
            self.__marks=0
            print("Marks Invalid") 
  
    def get_marks(self):
        print("The student marks are ",self.__marks)

student1=Student_Marks(20)
student1.set_marks(100)
student1.get_marks()        
