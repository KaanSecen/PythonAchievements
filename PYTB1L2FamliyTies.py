import os
import sys
from time import sleep

os.system("")

# Dit zorgt voor de kleur codes
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# Variabelen
naam = input(style.GREEN + "Wat is jou naam?\n> ")
leefttijd = input(style.YELLOW + "Wat is jou leeftijd?\n> ")
woonplaats = input(style.MAGENTA + "Wat is jou woonplaats?\n> ")
afstand = input (style.GREEN + "Wat is jou aftstand naar school?\n> ")
hobby = input(style.CYAN + "Wat is jou hobby?\n> ")

# Output
print("Hallo",naam,"jij bent dus",leefttijd,"jaar.\nJe woont in",woonplaats,"en jij woont",afstand,"kilometer van het Mediacollege.\nJou hobby is",hobby)
