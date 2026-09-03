class Person:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def display(self):
        print(f"{self.name} is {self.age} years old with {self.gpa} gpa")

class Student(Person):
    def __init__(self, name, age, gpa , rollno):
        super().__init__(name, age, gpa)
        self.rollno = rollno
    def display(self):
        print(f"{self.name} is {self.age} years old with {self.gpa} gpa and has a {self.rollno} rollno")


student = Student("Jame", 21, 3.2,rollno="24K-3069")
student.display()