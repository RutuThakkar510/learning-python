fruits = ['apple', 'banana', 'orange', 'grapes']

# for length
# for adding variable in string
print(f"length of the array is {len(fruits)}")

# access list
print(fruits[1]) # banana

# modifying list
fruits[1] = 'mango'
print(fruits) # ['apple', 'mango', 'orange', 'grapes']

#append
fruits.append('kiwi')
print(fruits)

fruits.insert(1, 'strawberry')
print(fruits)