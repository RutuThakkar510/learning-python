class Car:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("Drive!")
class Plane:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("Fly!")

car1 = Car("xuv")
plane1 = Plane("Air India")

for i in (car1, plane1):
    i.move()

# inheritance class Polymorphism

class Vehicle:
    def __init__(self, name):
        self.name = name
    def move(self):
        print(f"{self.name} can move!")

v1 = Vehicle("mustang")
# v1.move()

class Car(Vehicle):
    pass

c1 = Car("bmw")
# c1.move()

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} can fly!")

p1 = Plane("Air India")
# p1.move()

for x in (v1, c1, p1):
    print(f"name: {x.name}")
    x.move()