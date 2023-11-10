mylist = [1,2,3,4,5]
print(mylist)

# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
mystring = st.split()
for str in mystring:
    if(str[0] == 's'):
        print(str)

#Use range() to print all the even numbers from 0 to 10.
for i in range(0,11):
    if(i%2==0):
        print(i)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
mylist = [ num for num in range(1,51) if num%3==0]
print(mylist) # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

# Go through the string below and if the length of a word is even print "even!"
mylist = st.split()
for word in mylist:
    if(len(word)%2==0):
        print('even!')

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
comList = [letter[0] for letter in st.split()]
print(comList)

