import random


def choose_winner():
    return random.randint(1, 3)

def choose_door():
    return random.randint(1, 3)

# def keep_playing():
#     game_continue = input("Would you like to play again? Y/n: ").lower()
#     if game_continue == 'y':
#         return True
#     elif game_continue != 'n' and game_continue != 'y':
#         print("That's not one of the choices, try again")
#         return keep_playing()
#     else:
#         return False

def game_loop(game_status):
    for _ in range(100):
        winner = choose_winner()
        user_input = choose_door()
        print(user_input)
        if user_input > 3:
            print("There are not that many doors. What's wrong with you?")
            game_loop(game_status)
        if user_input == winner:
            print("Congratulations! You won the car!")
        if user_input != winner:
            print("I'm sorry, all you got was this stupid goat.")

def main():
    game_status = True
    game_loop(game_status)
main()
