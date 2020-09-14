import os
import sys
from time import sleep

os.system("")

# Deze functie telt/deelt/trekt af  bijde cijfers op
def plus(x, y):
    return x + y

def min(x, y):
    return x - y

def keer(x, y):
    return x * y

def delen(x, y):
    return x / y

# Deze functie zorgt voor de kleur codes
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


rekenmachine1 = style.CYAN + "Slimme rekenmachine:\n"
ber1 = style.RED + "De eerste is (+) (plus)\n"
ber2 = style.GREEN + "Welk getal wil je eerst gebruiken?\n"
ber3 = style.GREEN + "Daarna?\n"

tweede = style.RED + "De tweede is (-) (min)\n"
derde = style.RED + "De derde is (*) (keer)\n"
vierde = style.RED + "De vierde is (/) (delen)\n"

end1 = style.RESET + "Gemaakt door Kaan Secen\n"

for char in rekenmachine1:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in ber1:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in ber2:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

num1plus = float(input(">"))

for char in ber3:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

num2plus = float(input(">"))   

antw1 = "Antwoord:"

for char in antw1:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

print(style.CYAN)
print(plus(num1plus,num2plus))

for char in tweede:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in ber2:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

num1min = float(input(">"))

for char in ber3:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

num2min = float(input(">"))   

for char in antw1:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

print(style.CYAN)
print(min(num1min,num2min))

for char in derde:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in ber2:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

num1keer = float(input(">"))

for char in ber3:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

num2keer = float(input(">"))   

for char in antw1:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

print(style.CYAN)
print(keer(num1keer,num2keer))

for char in vierde:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in ber2:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

num1delen = float(input(">"))

for char in ber3:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

num2delen = float(input(">"))   

for char in antw1:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

print(style.CYAN)
print(delen(num1delen,num2delen))

for char in end1:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()