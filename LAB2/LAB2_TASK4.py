class Employee:
    def work(self):
        print("Employee is working")


class Manager(Employee):
    def work(self):
        print("Manager is managing the team")


class Developer(Employee):
    def work(self):
        print("Developer is writing code")


class Designer(Employee):
    def work(self):
        print("Designer is designing")


employees = [Manager(), Developer(), Designer()]

for employee in employees:
    employee.work()