import random
import os
import operator

import gspread
from google.oauth2.service_account import Credentials
from .utils import delay_print, clear_terminal

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('riddle_me_batman')

high_scores = SHEET.worksheet('highscores')
scores = high_scores.get_all_records()
game_results = {}

current_word = ''
masked_word = ''


def update_highscores_sheet():
    keys = [str(eachvalue) for eachvalue in scores[0].keys()]
    values = [str(eachvalue) for eachvalue in scores[0].values()]
    update_results = [{'range': 'A1:Z1', 'values': [keys]},
                      {'range': 'A2:Z2', 'values': [values]}]
    high_scores.batch_update(update_results)


def logo():
    """
    Text for the game logo
    """
    delay_print("""
    
______  _      _      _  _        ___  ___       ______         _                              ___  
| ___ \(_)    | |    | || |       |  \/  |       | ___ \       | |                            |__ \ 
| |_/ / _   __| |  __| || |  ___  | .  . |  ___  | |_/ /  __ _ | |_  _ __ ___    __ _  _ __      ) |
|    / | | / _` | / _` || | / _ \ | |\/| | / _ \ | ___ \ / _` || __|| '_ ` _ \  / _` || '_ \    / / 
| |\ \ | || (_| || (_| || ||  __/ | |  | ||  __/ | |_/ /| (_| || |_ | | | | | || (_| || | | |  |_|  
\_| \_||_| \__,_| \__,_||_| \___| \_|  |_/ \___| \____/  \__,_| \__||_| |_| |_| \__,_||_| |_|  (_)  
                                                                                                    
                                                                                                    

    """, 2)


def show_robin(attempts):
    phases = [
                """
                    +---------------------------------+
                    |              Robin              |
                    |           +---------+           |
                    +---------------------------------+
                    |                |                |
                    |                |                |
                    |                O                |
                    |               /|\\               |
                    |               / \\               |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+""",
                """
                    +---------------------------------+
                    |              Robin              |
                    |           +---------+           |
                    +---------------------------------+
                    |                |                |
                    |                |                |
                    |                O                |
                    |               /|\\               |
                    |               /                 |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+""",
                """
                    +---------------------------------+
                    |              Robin              |
                    |           +---------+           |
                    +---------------------------------+
                    |                |                |
                    |                |                |
                    |                O                |
                    |               /|\\               |
                    |                                 |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+""",
                """
                    +---------------------------------+
                    |              Robin              |
                    |           +---------+           |
                    +---------------------------------+
                    |                |                |
                    |                |                |
                    |                O                |
                    |               /|                |
                    |                                 |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+""",
                """
                    +---------------------------------+
                    |              Robin              |
                    |           +---------+           |
                    +---------------------------------+
                    |                |                |
                    |                |                |
                    |                O                |
                    |                |                |
                    |                                 |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+""",
                """
                    +---------------------------------+
                    |              Robin              |
                    |           +---------+           |
                    +---------------------------------+
                    |                |                |
                    |                |                |
                    |                O                |
                    |                                 |
                    |                                 |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+""",
                """
                    +---------------------------------+
                    |              Robin              |
                    |           +---------+           |
                    +---------------------------------+
                    |                |                |
                    |                |                |
                    |                                 |
                    |                                 |
                    |                                 |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+""",
                """
                    +---------------------------------+
                    |              Robin              |
                    |           +---------+           |
                    +---------------------------------+
                    |                                 |
                    |                                 |
                    |                                 |
                    |                                 |
                    |                                 |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+"""
                ]
    return phases[attempts]


letters_box = """                    |    A B C D E F G H I J K L M    |
                    |    N O P Q R S T U V W X Y Z    |
                    |                                 |
                    +---------------------------------+
    """
