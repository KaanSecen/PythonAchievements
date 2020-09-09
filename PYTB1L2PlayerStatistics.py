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

playerchoose = style.WHITE + "Choose a Player:\n"
playerchoose1 = style.GREEN + "kaan | cemre | hakan | damla\n"
kaanstats = style.YELLOW + "\nName: Kaan Secen\nPosition: GOALKEEPER [GK]\n\nSTATS:\n81 DIV 82 REF\n81 HAN 52 SPE\n73 KIC 79 POS\n\n"
cemrestats = style.YELLOW + "\nName: Cemre Secen\nPosition: CENTER-BACK [CB]\n\nSTATS:\n46 PAC 38 DRI\n35 SHO 55 DEF\n39 PAS 84 PHY\n\n"
hakanstats = style.YELLOW + "\nName: Hakan Secen\nPosition: STRIKER [ST]\n\nSTATS:\n79 PAC 77 DRI\n80 SHO 27 DEF\n59 PAS 74 PHY\n\n"
damlastats = style.YELLOW + "\nName: Damla Secen\nPosition: CENTER-BACK [CB]\n\nSTATS:\n68 PAC 49 DRI\n60 SHO 72 DEF\n70 PAS 89 PHY\n\n"
end = style.WHITE + "Gemaakt door Kaan Secen\n"

for char in playerchoose:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

for char in playerchoose1:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

result=input('>')
if result=='kaan':
     sleep(0.5)
     sys.stdout.write(kaanstats)
     sys.stdout.flush()
if result=='cemre':
     sleep(0.5)
     sys.stdout.write(cemrestats)
     sys.stdout.flush()
if result=='hakan':
     sleep(0.5)
     sys.stdout.write(hakanstats)
     sys.stdout.flush()
if result=='damla':
     sleep(0.5)
     sys.stdout.write(damlastats)
     sys.stdout.flush()

for char in end:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()