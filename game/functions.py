""" Imports for game functionality """
import random
import operator
import sys

from .utils import delay_print, clear_terminal
from .words import word_list
from .data import logo, show_robin, \
    LETTERS_BOX, scores, game_results, \
    update_highscores_sheet


def get_word():
    """
    Function that randomizes word_list
    """
    word = random.choice(word_list)
    return word.upper()


def welcome_screen():
    clear_terminal()
    logo()
    print("\n" * 2)
    delay_print("{:^70}".format("1: PLAY GAME"), 1)
    delay_print("{:^70}".format("2: HIGH SCORES"), 1)
    delay_print("{:^70}".format("3: EXIT"), 1)
    print("\n" * 2)

    while True:
        welcome_screen_choice = input("  " * 11 + "Please choose an option : ")
        if welcome_screen_choice == "1":
            player_name()
        elif welcome_screen_choice == "2":
            clear_terminal()
            print("{:^70}".format("HIGH SCORES : "))
            print("\n")
            ordered_scores = (dict(sorted(scores[0].items(),
                              key=operator.itemgetter(1), reverse=True)[:5]))
            for key, val in ordered_scores.items():
                print("{:^70}".format(f"{key} : {val}"))
                print("\n")

            while True:
                if input("  " * 12 +
                         " GO BACK TO MAIN MENU?(Y) : ").upper() == "Y":
                    clear_terminal()
                    welcome_screen()
                else:
                    print("{:^70}".format("Please Try Again"))
        elif welcome_screen_choice == "3":
            clear_terminal()
            sys.exit()
        else:
            print("{:^70}".format("Please Choose option 1, 2 or 3"))


def player_name():
    clear_terminal()
    attempts = 0
    delay_print("{:^78}".format("Riddle Me Batman ?"), 1)
    delay_print(show_robin(attempts), 1)
    delay_print(LETTERS_BOX, 1)
    global player
    letters_box2 = LETTERS_BOX
    while True:
        player = input("  " * 10 + " Please enter a Username: ").upper()
        if player.isalpha():
            game_results[player] = 0
            play(get_word(), letters_box2)
        else:
            print("{:^74}".format("Please use letters only"))


def replace_guess(word, HIDDEN_WORD, guess):
    index = 0
    HIDDEN_WORD = list(HIDDEN_WORD)
    for letter in word:
        if letter.upper() == guess.upper():
            HIDDEN_WORD[index] = guess
        index = index + 1
    return ''.join(HIDDEN_WORD)


def check_if_guess_in_word(guess, word):
    return guess.upper() in word.upper()


def validate_guess(guess, guessed_letters):
    if (len(guess) == 1) and guess.isalpha() and (
       guess not in guessed_letters):
        return True
    if guess in guessed_letters:
        print("You've already guessed the letter: " + guess)
    if guess.isalpha() is False:
        print("Guess is not valid, please try again.")
    return False


def play(word, LETTERS_BOX):
    letters_box2 = LETTERS_BOX
    clear_terminal()
    completed_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    attempts = 7

    print(show_robin(attempts))
    print(letters_box2)
    print(completed_word)

    while not guessed and attempts > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == len(word):
            if check_if_guess_in_word(guess, word) is False:
                print("Sorry " + guess + " is not the word.")
                attempts -= 1
            else:
                guessed = True
        else:
            if validate_guess(guess, guessed_letters):
                guessed_letters.append(guess)
                letters_box2 = letters_box2.replace(guess.upper(), '*')
                if check_if_guess_in_word(guess, word):
                    completed_word = replace_guess(word, completed_word, guess)
                    print("Well done!", guess, "is in the word.")
                    if completed_word.upper() == word.upper():
                        guessed = True
                else:
                    print("Sorry " + guess + " is not in the word.")
                    attempts -= 1
            else:
                if guess.isalpha():
                    letters_box2 = letters_box2.replace(guess.upper(), '*')
                if check_if_guess_in_word(guess, completed_word) is False:
                    attempts -= 1

        print(show_robin(attempts))
        print(letters_box2)
        print(completed_word)

    if guessed:
        clear_terminal()
        print("You just saved Robin! " + player +
              ", you are an amazing riddle solver! \n")

        while True:
            play_again_after_win = input('  ' +
                                         ' Play Again? ( Y / N ) : ').upper()
            if play_again_after_win == 'Y':
                game_results[player] += 1
                play(get_word(), LETTERS_BOX)
            elif play_again_after_win == 'N':
                game_results[player] += 1
                if player not in scores[0].keys():
                    scores[0][player] = game_results[player]
                    update_highscores_sheet()
                    welcome_screen()
                elif game_results[player] > scores[0][player]:
                    scores[0][player] = game_results[player]
                    update_highscores_sheet()
                    welcome_screen()
                else:
                    welcome_screen()
    else:
        print("Sorry " + player + ", you died")
        print("the word was " + word + ", better luck next time!")

        while True:
            play_again_after_lose = input('  ' * 10 +
                                          ' Play Again? ( Y / N ) : ').upper()
            if play_again_after_lose == 'Y':
                play(get_word(), LETTERS_BOX)
            elif play_again_after_lose == 'N':
                welcome_screen()
            else:
                print('{:^70}'.format(' Please choose option Y or N '))


def main():
    """
    The main game loop
    """
    letters_box2 = LETTERS_BOX
    welcome_screen()
    CURRENT_WORD = get_word()
    play(CURRENT_WORD, letters_box2)
    while input("Play again? (Y/N) ").upper() == "Y":
        letters_box2 = LETTERS_BOX
        word = get_word()
        play(word, letters_box2)
        welcome_screen()


if __name__ == "__main__":
    main()
