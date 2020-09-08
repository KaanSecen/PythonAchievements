import os
import sys
from time import sleep

os.system("")


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

vers1type = style.RED + "Hallo mijn naam is Kaan. \n"
vers2type = style.GREEN + "Ik ben met de bus hier naar toe gegaan. \n"
vers3type = style.YELLOW + "Mijn woonplaats is Amsterdam Noord. \n"
vers4type = style.BLUE + "Ik vertel nooit mijn wachtwoord. \n"
vers5type = style.MAGENTA + "Mensen helpen doe ik graag. \n"
vers6type = style.CYAN + "Want mensen hebben mij om hulp gevraagd. \n"
vers7type = style.WHITE + "Later wil ik heel erg veel poen. \n"
vers8type = style.YELLOW + "Met programmeren wil ik Later iets doen. \n"
versmaaks = style.RESET + "Gemaakt Door Kaan Secen. \n \n"


for char in vers1type:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in vers2type:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in vers3type:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in vers4type:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in vers5type:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in vers6type:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in vers7type:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in vers8type:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in versmaaks:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()


vers1 = "Hallo mijn naam is Kaan."
vers2 = "Ik ben met de bus hier naar toe gegaan."
vers3 = "Mijn woonplaats is Amsterdam Noord."
vers4 = "Ik vertel nooit mijn wachtwoord."
vers5 = "Mensen helpen doe ik graag."
vers6 = "Want mensen hebben mij om hulp gevraagd."
vers7 = "Later wil ik heel erg veel poen."
vers8 = "Met programmeren wil ik Later iets doen."

print(vers1)
print(vers2)
print(vers3)
print(vers4)
print(vers5)
print(vers6)
print(vers7)
print(vers8)
print("Gemaakt Door Kaan Secen.")