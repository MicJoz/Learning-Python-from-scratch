import random


def making_choice():
    choice_to_check = int(input("\nTo play a game --> enter: 1\nTo quit --> enter: 2\n\nMake your choice: "))

    while choice_to_check != 1 and choice_to_check != 2:
        choice_to_check = int(input("Invalid number. Make your choice again: "))

    if choice_to_check == 1:
        playing_game()
    else:
        print("\nThank you for playing!")


def playing_game():
    player_weapon = int(input(f"\n 1. Rock\n 2. Paper\n 3. Scissors\nChoose your weapon: "))
    if player_weapon == 1:
        print(f"\nYou chose Rock.")
    elif player_weapon == 2:
        print(f"\nYou chose Paper.")
    elif player_weapon == 3:
        print(f"\nYou chose Scissors.")

    computer_weapon = random.randint(1, 3)
    if computer_weapon == 1:
        print(f"Computer chose Rock.")
    elif computer_weapon == 2:
        print(f"Computer chose Paper.")
    elif computer_weapon == 3:
        print(f"Computer chose Scissors.")

    print("\nLet the battle begin!\n")

    if player_weapon == computer_weapon:
        print("It's a draw.")
    elif player_weapon == 1 and computer_weapon == 3 or player_weapon == 2 and computer_weapon == 1 or player_weapon == 3 and computer_weapon == 2:
        print("You win!")
    else:
        print("You lose! Better luck next time.")

    making_choice()


print("\nWelcome to Rock, Paper, Scissors")

making_choice()
