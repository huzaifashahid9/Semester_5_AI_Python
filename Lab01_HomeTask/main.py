#Task 1

student = ('Nadeem', 28, 3.75)
student[1] = 24

# A list can be updated, but a tuple cannot
# TypeError

def show(name, age):
    print('Name : ', name)
    print('Age : ', age)

show("Nadeem", 20)
#logical error
#Order should be always right
age_entered = int(input('Enter age: ')
)
#TypeError
#Type int is necessary because str and int cant compare
if age_entered > 18:
    print('Adult')

marks = [90, 85, 78]
total = sum(marks)
#NameError
#total missing
print('Average : ', total / 3)