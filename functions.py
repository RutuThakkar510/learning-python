def greet():
    print("Hello from the Python!")

greet()

# print sum of two no. (passed in args)
def addition(a: int,b: int):
    print(a + b)

addition(1,2)

# return
def subtract(a: int,b: int):
    return a - b

result = subtract(10,5)
print(result)

def display(*num):
    print(num)

display(1,2,3)