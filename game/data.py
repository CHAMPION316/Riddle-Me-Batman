import gspread
from google.oauth2.service_account import Credentials

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

def logo():
    """
    Text for the game logo
    """
    print("""
    
______  _      _      _  _        ___  ___       ______         _                              ___  
| ___ \(_)    | |    | || |       |  \/  |       | ___ \       | |                            |__ \ 
| |_/ / _   __| |  __| || |  ___  | .  . |  ___  | |_/ /  __ _ | |_  _ __ ___    __ _  _ __      ) |
|    / | | / _` | / _` || | / _ \ | |\/| | / _ \ | ___ \ / _` || __|| '_ ` _ \  / _` || '_ \    / / 
| |\ \ | || (_| || (_| || ||  __/ | |  | ||  __/ | |_/ /| (_| || |_ | | | | | || (_| || | | |  |_|  
\_| \_||_| \__,_| \__,_||_| \___| \_|  |_/ \___| \____/  \__,_| \__||_| |_| |_| \__,_||_| |_|  (_)  
                                                                                                    
                                                                                                    

    """)