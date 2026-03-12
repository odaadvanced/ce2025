class Person():
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"Hi, my name is {self.name}")
    
class Student(Person):
    def __init__(self, name, grade_level):
        self.name = name
        self.grade_level = grade_level
    def introduce(self):
        print(f"Hi, my name is {self.name}, and I am in grade {self.grade_level}")

man = Person("robert")
student = Student("joe", 8)