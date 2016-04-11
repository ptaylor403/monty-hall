import random

def choose_winner():
    return random.randint(1, 3)

def choose_door():
    return random.randint(1, 3)

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

    print("Ran game 2000 times. \nCar {}, Goat {}.".format(times_won, got_goat))
def main():
    game_loop()
main()
