from .data import logo
from .utils import delay_print, clear_terminal

def welcome_screen():
    logo()


def main():
    """
    The main game loop
    """
    welcome_screen()