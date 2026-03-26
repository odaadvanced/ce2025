class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"{self.name}'s age is {self.age}")

class Teacher(SchoolMember):
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject
    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")
    def display_info(self):
        print(f"Teacher: {self.name}, Age: {self.age}, Subject: {self.subject}")

class Student(SchoolMember):
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def study(self):
        print(f"{self.name} is studying for grade {self.grade} classes.")
    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}")

bob = Teacher("Mr. Bob", 45, "math")

john = Student("John", 7, 2)
gerald = Student("Gerald", 11, 4)

bob.display_info()
john.display_info()
gerald.display_info()

bob.teach()
john.study()
gerald.study()