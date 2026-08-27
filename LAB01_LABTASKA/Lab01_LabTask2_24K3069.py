semesterResult = [
    ("LA", 80),
    ("ISE", 72),
    ("COAL", 99),
    ("DAA", 54),
    ("AI", 81),
    ("EBW", 67)
]

grade_count = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0
}

total_marks = 0
valid_subjects = 0
invalid = 0

print("Subject\tMarks\tGrade")

for subject, marks in semesterResult:

    if marks < 0 or marks > 100:
        print(subject, "\tInvalid")
        invalid += 1
        continue

    if marks >= 85:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    print(subject, "\t", marks, "\t", grade)

    grade_count[grade] += 1

    total_marks += marks
    valid_subjects += 1


average = total_marks / valid_subjects

print("\nGrade Summary:")
print(grade_count)

print("Invalid entries:", invalid)
print("Average:", average)