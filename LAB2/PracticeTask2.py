class Staff:

    def __init__(self, name, staff_id , department):
        self.name = name
        self.staff_id = staff_id
        self.department = department

    def display_info(self):
            print(f"--- Staff {self.name} Profie")
            print(f"Staff ID: {self.staff_id}")
            print(f"Department: {self.department}")

class Teacher(Staff):
    def __init__ (self ,name, staff_id , department, courses , salary ):
        super().__init__(name, staff_id, department)
        self.courses = courses
        self.salary = salary

    def teach_courses(self):
            print(f"--- Teacher {self.name} is current teaching :{', '.join(self.courses)}")

    def display_info(self):
            super().display_info()
            print(f" Role : Teacher")
            print(f" Salary : {self.salary}")
            print(f" Courses: {', '.join(self.courses)}")
            print("_" * 20)

class AdministrativeStaff(Staff):
    def __init__(self, name, staff_id , department, role ,workingHour):
        super().__init__(name, staff_id, department)
        self.role = role
        self.workingHour = workingHour

    def perform_tasks(self):
        print(f" {self.name} is performing administrative tasks as a {self.role}")

    def display_info(self):
        super().display_info()
        print(f" Role : {self.role}")
        print(f" Working Hour: {self.workingHour}")
        print("_" * 20)

class ResearchAssistants(Staff):
    def __init__(self, name, staff_id , department ,research_topic , stipend):
        super().__init__(name, staff_id, department)
        self.research_topic = research_topic
        self.stipend = stipend

    def work_on_research(self):
        print(f" {self.name} is working on research assistants as a {self.research_topic}")

    def display_info(self):
        super().display_info()
        print(f" Role : Research Assistant")
        print(f" Research Topic: {self.research_topic}")
        print(f" Stipend: {self.stipend}")
        print("_" * 20)

teacher1 = Teacher(
    "Ali",
    "T001",
    "Computer Science",
    ["Python", "Database"],
    80000
)

admin1 = AdministrativeStaff(
    "Sara",
    "Administration",
    "Computer Science",
    "Office Manager",
    40
)

researcher1 = ResearchAssistants(
    "Ahmed",
    "R001",
    "Computer Science",
    "Artificial Intelligence",
    50000
)

teacher1.display_info()
admin1.display_info()
researcher1.display_info()

print("Daily Achievement")
teacher1.teach_courses()
admin1.perform_tasks()
researcher1.work_on_research()
