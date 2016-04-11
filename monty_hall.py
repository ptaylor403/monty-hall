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

def no_change_game_loop():
    win = 0
    lose = 0
    for _ in range(1000):
        winner = choose_winner()
        first_choice = choose_door()
        open_other = change_choice(first_choice)
        if open_other != winner:
            lose += 1
        if open_other == winner:
            win += 1
    print("\nNot changing choice. \nCar {}%, Goat {}%.".format((win / 10), (lose / 10)))

def change_game_loop():
    times_won = 0
    got_goat = 0
    for _ in range(1000):
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

    print("\nChanging your choice. \nCar {}%, Goat {}%.".format((times_won / 10), (got_goat / 10)))

def main():
    no_change_game_loop()
    change_game_loop()

main()
