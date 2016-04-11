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

def change_choice(choice):
    new_choice = random.randint(1,3)
    if new_choice == choice:
        return change_choice(choice)
    else:
        return new_choice

def game_loop():
    times_won = 0
    got_goat = 0
    for _ in range(2000):
        winner = choose_winner()
        first_choice = choose_door()
        open_other = change_choice(first_choice)
        if open_other != winner:
            second_choice = change_choice(open_other)
            if second_choice == winner:
                times_won += 1
            if second_choice != winner:
                got_goat += 1
        else:
            times_won += 1

        # print("first", first_choice)
        # print("second", second_choice)
        # if user_input > 3:
        #     print("There are not that many doors. What's wrong with you?")
        #     game_loop(game_status)

        #     print("Congratulations! You won the car!")
        # if user_input != winner:
        #     print("I'm sorry, all you got was this stupid goat.")
    print("Ran game 2000 times. \nCar {}, Goat {}.".format(times_won, got_goat))
def main():
    game_loop()
main()
