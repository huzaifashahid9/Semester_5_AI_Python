name = input("Enter your name: ")
age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))

courses = input("Enter courses: ").split()

student = {
    "name": name,
    "age": age,
    "cgpa": cgpa,
    "courses": courses
}

print("-" * 30)
print("STUDENT PROFILE")
print("-" * 30)

print("Name:", student["name"])
print("Age:", student["age"])
print("CGPA:", student["cgpa"])
print("Courses:", student["courses"])

print("-" * 30)
print("TYPE REPORT")
print("-" * 30)

for key in student:
    print(key, ":", student[key], "Type:", type(student[key]))

print("-" * 30)

print("Initials:", name[0])

print("-" * 30)