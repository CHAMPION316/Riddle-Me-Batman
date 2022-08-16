from .utils import delay_print, clear_terminal
from words import word_list
from .data import logo, current_word, masked_word


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


def main():
    """
    The main game loop
    """
    welcome_screen()
