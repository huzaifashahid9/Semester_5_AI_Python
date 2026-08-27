# Error 1: TypeError
# A tuple cannot modify the existing tuple
# Creating a new tuple keeps the student record as a tuple
student = ('Nadeem', 28, 3.75)
student = (student[0], 24, student[2])

# Error 2: Syntax error
# The statements inside the function must be ordered
def show(name, age):
    print('Name:', name)
    print('Age:', age)


# Error 3: Logical error
# The function expects name first and age second the arguments must be
# passed in the correct order
show(student[0], student[1])


# Error 4: TypeError
# int() converts the entered value into an integer
age_entered = int(input('Enter age: '))

# Error 5: Syntax error
# The statement inside the if block must be indented
if age_entered > 18:
    print('Adult')


marks = [90, 85, 78]

# Error 6: NameError
# The variable total was used before being defined
total = sum(marks)

print('Average:', total / 3)