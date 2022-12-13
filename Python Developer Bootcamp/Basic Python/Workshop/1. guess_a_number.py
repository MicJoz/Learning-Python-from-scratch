import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        player_number = int(input("Guess the number: "))
        break
    except ValueError:
        print("It's not a number!")

is_guessed = False

while not is_guessed:
    if player_number < number_to_guess:
        print("Too small!")
        player_number = int(input("Guess the number: "))
    elif player_number > number_to_guess:
        print("Too big!")
        player_number = int(input("Guess the number: "))
    else:
        print("You win!")
        is_guessed = True

