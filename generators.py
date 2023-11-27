# more memory efficient
def create_cubes(n):
    for x in range(n):
        yield x**3

print(list(create_cubes(10))) # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# fibonacci series
def get_fibo(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+b

print(list(get_fibo(10)))
