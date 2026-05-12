def obj_methods(obj):
    return [method_name for method_name in dir(obj) if callable(getattr(obj, method_name))]

class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"

class Terrier(Dog):
    pass
class Collie(Dog):
    def speak(self, sound = 'Bow wow'):
        return f"{self.name} says {sound}"
class Bulldog(Dog):
    def describe(self):
        return f"{self.name} has short hair"

collie = Collie('lassie',2)
bill = Bulldog('bill', 4)
print('the end')