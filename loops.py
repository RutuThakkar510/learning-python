# for loop
# loop through list
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

# loop through range
for i in range(0,6):

    print(i)

# loop through list of tuples
myList = [(1,2), (3,4), (5,6), (7,8)]
for a,b in myList:
    print(a)
    print(b)

for tup in myList:
    print(tup)

# loop through dictionary
d = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}
# only loop through keys
for item in d:
    print(item)

# loop through key and value pairs
for k,v in d.items():
    print(k)
    print(v)

# loop through value
for v in d.values():
    print(v)

# while loop
while len(fruits) > 0:
    print(fruits)
    fruits = fruits[1:(len(fruits))]

# while else
x=0
while x < 5:
    print(f'the current value is {x}')
    x +=1
else:
    print(f'{x} is  not less than 5')

myList = []
mystring = "Hello World!"

for letter in mystring:
    myList.append(letter)
print(myList) #['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']

myList = [letter for letter in mystring]
print(myList) #['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']

myList = []
for num in range(10):
    myList.append(num)
print(myList) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

myList = [num**2 for num in range(1,11)]
print(myList) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# add condition
myList= [num for num in range(1,11) if num%2 == 0]
print(myList)

