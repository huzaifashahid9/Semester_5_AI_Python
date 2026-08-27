knowledge_base = {
    "python": "Python is used in AI Lab.",
    "grading": "Please check the grading rubric.",
    "project": "The project details are available from your instructor."
}


def match_rule(question, knowledge_base):

    question = question.lower()

    for keyword in knowledge_base:
        if keyword in question:
            return knowledge_base[keyword]

    return None


def session_report(*questions, **stats):

    print("\n----- SESSION REPORT -----")

    print("\nQuestions Asked:")

    for question in questions:
        print("-", question)

    print("\nStatistics:")

    for key in stats:
        print(key, ":", stats[key])

    return None


name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\nHello", name, "Welcome to AI Lab Advisor!")


questions = []

matched = 0
unmatched = 0


while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    questions.append(question)

    answer = match_rule(question, knowledge_base)

    if answer is not None:
        print("Answer:", answer)
        matched += 1

    else:
        print("Sorry, I do not have information about that.")
        unmatched += 1


session_report(
    *questions,
    matched=matched,
    unmatched=unmatched
)