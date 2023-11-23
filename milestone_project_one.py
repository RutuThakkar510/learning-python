# def my_func(row1, row2, row3):
#     print(row1)
#     print(row2)
#     print(row3)

# row1 = [" ", " ", " "]
# row2 = [" ", " ", " "]
# row3 = [" ", " ", " "]
# row2[1] = 'X'
# my_func(row1, row2, row3)

# # index_position = int(input("Enter the index position: "))
# # print(index_position)

# def user_choice():
#     choice = ''
#     acceptable_range = range(0,10)
#     within_range = False

#     while choice.isdigit() == False or within_range == False:
#         choice = input("Please enter a number (0-10): ")
#         if choice.isdigit() == False:
#             print("Sorry! invalid input, entered value is not a digit.")
#         else:
#             if int(choice) in acceptable_range:
#                 within_range = True
#             else:
#                 print("Sorry! invalid input, entered value is out of range.")
#                 pass
#     return int(choice)

# print(type(user_choice()))


game_list = [0, 1, 2]
def display_game(game_list):
    print(f'current game list is: {game_list}')

display_game(game_list)

def position_choice():
    choice = ''
    acceptable_range = ['0', '1', '2']
    while choice not in acceptable_range:
        choice = input('Please enter a number (0-2)')
        if choice not in acceptable_range:
            print('Sorry, Invalid input')
    
    return int(choice)

choice = position_choice()

def replacement_choice(game_list, position):
    replacement_value = input('Please enter a replacement value: ')
    game_list[position] = replacement_value
    return game_list

game_list = replacement_choice(game_list, choice)
display_game(game_list)