
import os

import datetime

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



def remove_file(file):
    if os.path.exists(file):
        os.remove(file)


def to_sql_string(chaine: str):
    return f"'{chaine}'"


def chaine_is_valid(chaine: str) -> bool:
    return  chaine and not chaine.isspace()