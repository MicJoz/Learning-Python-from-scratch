import random
from hangman_pics import hangman_stages
from hangman_pics import hangman_logo
from words_to_guess import words_list


def making_choice():
    choice_to_check = int(input("\nTo play a game --> enter: 1\nTo quit --> enter: 2\n\nMake your choice: "))

    while choice_to_check != 1 and choice_to_check != 2:
        choice_to_check = int(input("Invalid number. Make your choice again: "))

    if choice_to_check == 1:
        guessing_word()
    else:
        print("\nThank you for playing!")


def guessing_word():
    word_to_guess = random.choice(words_list)
    print(f'\n*** For testing purposes only: word to be guessed is "{word_to_guess}" ***\n')
    print(f"Word to be guessed consists of {len(word_to_guess)} letters.")

    game_display = []
    for i in word_to_guess:
        game_display += "_"
    print(" ".join(game_display))

    guesses = 6
    wrong_letters = []
    game_over = False

    while not game_over:
        guessed_letter = input("Enter a letter: ")

        if guessed_letter in game_display:
            print(f'You have already guessed a letter "{guessed_letter}".')
        elif guessed_letter in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guessed_letter:
                    game_display[i] = guessed_letter
            print(" ".join(game_display))
            if "_" not in game_display:
                print("\nWell done. You win!")
                game_over = True
        elif guessed_letter in wrong_letters:
            print(f'You have already tried a letter "{guessed_letter}".')
        else:
            guesses -= 1
            print(f'Ups. There is no letter "{guessed_letter}".')
            wrong_letters.append(guessed_letter)
            print(hangman_stages[guesses])
            if guesses > 1:
                print(f"You have {guesses} guesses left.")
            elif guesses == 1:
                print(f"You have only {guesses} guess left.")
            else:
                print("No more guesses. You lose!")
                print(f'Word to be guessed was "{word_to_guess}". More luck to you next time.')
                game_over = True

    making_choice()


print("\nWelcome to Hangman")
print(hangman_logo)

making_choice()
