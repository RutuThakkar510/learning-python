#LESSER OF TWO EVENS: 
'''Write a function that returns the lesser of two given numbers if both numbers are even, 
but returns the greater if one or both numbers are odd'''

def my_func(num1, num2):
    temp = 0
    if (num1 % 2 == 0 and num2 % 2 == 0):
        if (num1 > num2):
            return num2
        else:
            return num1
    else:
        if (num1 > num2):
            return num1
        else:
            return num2
# num = my_func(2,4)
num = my_func(2,3)
print(num)


'''ANIMAL CRACKERS:
Write a function takes a two-word string and returns True if both words begin with same letter'''
def animal_crackers(text):
    temp = text.split(' ')
    if temp[0][0] == temp[1][0]:
        return True

animal_crackers('Leo Leo')

'''MAKES TWENTY:
Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
If not, return False'''

def my_func(num1, num2):
    if num1 == 20 or num2 == 20 or sum((num1,num2)) == 20:
        return True
    else:
        return False

print(my_func(10,10))

'''OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name'''
def old_macdonald(name):
    oth = name[0]
    first = name[1:3]
    sec = name[3]
    third = name[4:]
    temp = oth.upper() + first + sec.upper() + third
    print(temp)
     #another solution
    temp = name[:3].capitalize()+name[3:].capitalize()
    print(temp)

old_macdonald('macdonald')

'''MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
'''

def master_yoda(text):
    word = text.split()
    reserved_list = word[::-1]
    reserved = ' '.join(reserved_list)
    print(reserved)

    # another solution
    reversed_word = ' '.join(text.split()[::-1])
    print(reversed_word)

master_yoda('Hello Here I am')