# class MyClass:
#     x=10

# create object
# p1 = MyClass()
# print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"I am {self.name}, age is {self.age}"
    def welcome(self):
        print(f"Welcome {self.name}")
    def myFunc(self):
        print(f"Hello, {self.name}, age is {self.age}")

p1 = Person("John", 36)

print(p1)
p1.myFunc()
print(p1.name)
print(p1.age)
p1.age = 23 # we can change object
print(p1.age)
        
# class Student(Person):
#     pass

class Student(Person):
    def __init__(self, name, age, city):
        super().__init__(name, age)
        self.city = city
    def welcome(self):
        print(f"welcome {self.name}, age is {self.age}")
    def myFunc2(self):
        # print(f"Hello, {self.name}, age is {self.age} and city is {self.city}")
        return f"Hello, {self.name}, age is {self.age} and city is {self.city}"

s1 = Student("Hannah", 22, "Ahmedabad")
s1.myFunc()
s1.welcome()
print(s1.myFunc2())

