rules = {
    "IT Support": ["wifi", "laptop", "password"],
    "Accounts": ["fee", "payment"],
    "Academic Office": ["course", "registration"]
}

complaints = [
    ("wifi is not working", "IT Support"),
    ("forgot my password", "IT Support"),
    ("laptop is broken", "IT Support"),
    ("fee payment problem", "Accounts"),
    ("payment is pending", "Accounts"),
    ("course registration problem", "Academic Office"),
    ("I want to change my course", "Academic Office"),
    ("I have a question", "General Office")
]


def route(complaint, rules, fallback="General Office"):

    for department in rules:
        for keyword in rules[department]:
            if keyword in complaint:
                return department

    return fallback


def evaluate(*results, **info):

    correct = results.count(True)
    incorrect = results.count(False)

    print("\nCorrect:", correct)
    print("Incorrect:", incorrect)

    for key in info:
        print(key, ":", info[key])


correct = 0
incorrect = 0
results = []
department_counts = {}


for complaint, true_department in complaints:

    predicted = route(complaint, rules)

    is_correct = predicted == true_department
    results.append(is_correct)

    if is_correct:
        correct += 1
        print(complaint, "->", predicted, "Correct")
    else:
        incorrect += 1
        print(complaint, "->", predicted, "Incorrect")

    if predicted in department_counts:
        department_counts[predicted] += 1
    else:
        department_counts[predicted] = 1


total = len(complaints)
accuracy = correct / total * 100

print("\nAccuracy:", accuracy, "%")
print("Department counts:", department_counts)


evaluate(
    *results,
    analyst="Khadeejah"
)