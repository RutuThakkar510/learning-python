import random
import string

passwordLength = int(input("Enter your password length: "))
print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')

characterList = ""
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        characterList += string.digits
    elif choice == 2:
        characterList += string.ascii_letters
    elif choice == 3:
        characterList += string.punctuation
    elif choice == 4:
        break
    else:
        print('Please pick a valid option') 

password = []
for i in range(passwordLength):
    randomChar = random.choice(characterList)
    # appending a random character to password
    password.append(randomChar)

print(f'strong password is generated for you :)  ' + "".join(password))



# print(random.random())
# print(string.digits)

# print(random.choices(string.digits))
