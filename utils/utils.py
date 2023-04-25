
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



def remove_file(file):
    if os.path.exists(file):
        os.remove(file)