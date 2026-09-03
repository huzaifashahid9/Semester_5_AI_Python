# class Student :
#     name = "Huzaifa Shahid"
#     age = 21
#
#     def displayStudent(self) :
#         print("Name: " , self.name)
#         print("Age: " , self.age)
#
#
# student1 = Student()
# student1.displayStudent()
#
# print(Student.name)
# print(Student.age)


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

person1 = Person("John", 20)
person1.display()
person2 = Person("Jame", 21)
person2.display()