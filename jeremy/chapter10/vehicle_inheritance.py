class Vehicle():
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def show_info(self):
        print(f"Brand: {self.brand}, Speed: {self.speed}")

class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        self.brand = brand
        self.speed = speed
        self.doors = doors
    def honk(self):
        print("Beep beep!")

my_vehicle = Vehicle("samsung", 10)
my_car = Car("ford", 200, 5)