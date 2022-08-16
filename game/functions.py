from .utils import delay_print, clear_terminal
from .words import word_list
from .data import logo, current_word, masked_word, show_robin, letters_box


def get_word():
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
    delay_print(show_robin(attempts))
    delay_print(letters_box)
    global player
    letters_box2 = letters_box
    while True:
        player = input("  " * 10 + " Please enter a Username: ").upper()
        if player.isalpha():
            game_results[player] = 0
            play(get_word(), letters_box2)
        else:
            print("{:^74}".format("Please use letters only"))


def replace_guess(word, masked_word, guess):
    index = 0
    masked_word = list(masked_word)
    for letter in word:
        if letter.upper() == guess.upper():
            masked_word[index] = guess
        index = index + 1
    return ''.join(masked_word)


def check_if_guess_in_word():
    return guess.upper() in word.upper()


def main():
    """
    The main game loop
    """
    letters_box2 = letters_box
    welcome_screen()
    current_word = get_word()
