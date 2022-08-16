from .data import logo
from .utils import delay_print, clear_terminal

def welcome_screen():
    clear_terminal()
    logo()
    print("\n" * 2)
    print("{:^70}".format("1: PLAY GAME"))
    print("{:^70}".format("2: HIGH SCORES"))
    print("{:^70}".format("3: EXIT"))
    print("\n" * 2)



def main():
    """
    The main game loop
    """
    welcome_screen()
