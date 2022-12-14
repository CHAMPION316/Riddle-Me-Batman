""" Imports for game functionality """
import random
import operator
import sys

from .utils import delay_print, clear_terminal
from .words import word_list
from .data import logo, show_robin, \
    game_letters, scores, game_results, \
    update_highscores_sheet


def get_word():
    """
    Function that randomizes word_list
    """
    word = random.choice(word_list)
    return word.upper()


def home_screen():
    """
    Home screen options and inputs
    for opening game
    """
    clear_terminal()
    logo()
    print("\n" * 2)
    delay_print("{:^70}".format("1: SAVE ROBIN (PLAY GAME)"), 1)
    delay_print("{:^70}".format("2: HIGH SCORES"), 1)
    delay_print("{:^70}".format("3: EXIT"), 1)
    print("\n" * 2)

    while True:
        home_screen_choice = input("  " * 11 + "Please choose an option : ")
        if home_screen_choice == "1":
            player_name()
        elif home_screen_choice == "2":
            clear_terminal()
            print("{:^70}".format("HIGH SCORE RIDDLE SOLVERS : "))
            print("\n")
            ordered_scores = (dict(sorted(scores[0].items(),
                              key=operator.itemgetter(1), reverse=True)[:5]))
            for key, val in ordered_scores.items():
                print("{:^70}".format(f"{key} : {val}"))
                print("\n")

            while True:
                if input("  " * 12 +
                         " RETURN TO MAIN MENU?(Y) : ").upper() == "Y":
                    clear_terminal()
                    home_screen()
                else:
                    print("{:^70}".format("Please Try Again"))
        elif home_screen_choice == "3":
            clear_terminal()
            sys.exit()
        else:
            print("{:^70}".format("Please Choose option 1, 2 or 3"))


def player_name():
    """
    Create player name to play game
    """
    clear_terminal()
    attempts = 0
    delay_print("{:^78}".format("Riddle Me Batman ?"), 1)
    delay_print(show_robin(attempts), 1)
    delay_print(game_letters, 1)
    global player
    letters_box2 = game_letters
    while True:
        player = input("  " * 10 + " Please enter a Username: ").upper()
        if player.isalpha():
            game_results[player] = 0
            play(get_word(), letters_box2)
        else:
            print("{:^74}".format("Please use letters only"))


def replace_guess(word, hidden_word, guess):
    """
    Replace guessed letter in word
    """
    index = 0
    hidden_word = list(hidden_word)
    for letter in word:
        if letter.upper() == guess.upper():
            hidden_word[index] = guess
        index = index + 1
    return ''.join(hidden_word)


def check_if_guess_in_word(guess, word):
    """
    Check if player guess is in word
    """
    return guess.upper() in word.upper()


def validate_guess(guess, guessed_letters):
    """
    Validate guessed letters in word
    """
    if (len(guess) == 1) and guess.isalpha() and (
       guess not in guessed_letters):
        return True
    if guess in guessed_letters:
        print(f"You've already guessed that letter {player}: " + guess)
    if guess.isalpha() is False:
        print("Guess is not valid, please try again.")
    return False


def play(word, game_letters):
    """
    Full gameplay functionality function
    """
    game_letters2 = game_letters
    clear_terminal()
    completed_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    attempts = 7

    print(show_robin(attempts))
    print(game_letters2)
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
                game_letters2 = game_letters2.replace(guess.upper(), '*')
                if check_if_guess_in_word(guess, word):
                    completed_word = replace_guess(word, completed_word, guess)
                    print(f"Good job {player}!", guess, "is in the word.")
                    if completed_word.upper() == word.upper():
                        guessed = True
                else:
                    print(f"Unfortunately {player}, " + guess + " is not in the word.")
                    attempts -= 1
            else:
                if guess.isalpha():
                    game_letters2 = game_letters2.replace(guess.upper(), '*')
                if check_if_guess_in_word(guess, completed_word) is False:
                    attempts -= 1

        print(show_robin(attempts))
        print(game_letters2)
        print(completed_word)

    if guessed:
        clear_terminal()
        print("You just saved Robin! \n " + player +
              ", you are an amazing riddle solver! \n")

        while True:
            play_again_after_win = input('  ' +
                                         ' Play Again? ( Y / N ) : ').upper()
            if play_again_after_win == 'Y':
                game_results[player] += 1
                play(get_word(), game_letters)
            elif play_again_after_win == 'N':
                game_results[player] += 1
                if player not in scores[0].keys():
                    scores[0][player] = game_results[player]
                    update_highscores_sheet()
                    home_screen()
                elif game_results[player] > scores[0][player]:
                    scores[0][player] = game_results[player]
                    update_highscores_sheet()
                    home_screen()
                else:
                    home_screen()
    else:
        print("Sorry " + player + ", you died")
        print("the word was " + word + ", better luck next time!")

        while True:
            play_again_after_lose = input('  ' * 10 +
                                          ' Play Again? ( Y / N ) : ').upper()
            if play_again_after_lose == 'Y':
                play(get_word(), game_letters)
            elif play_again_after_lose == 'N':
                home_screen()
            else:
                print('{:^70}'.format(' Please choose option Y or N '))


def main():
    """
    The main game loop
    """
    game_letters2 = game_letters
    home_screen()
    current_word = get_word()
    play(current_word, game_letters2)
    while input("Play again? (Y/N) ").upper() == "Y":
        game_letters2 = game_letters
        word = get_word()
        play(word, game_letters2)
        home_screen()


if __name__ == "__main__":
    main()
