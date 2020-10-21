from time import sleep
name = "Kaan Secen"
moneyInAccount = 200
inkomen = 250

script = True
winkel = False
vraag = True
sparen = False

while script == True:

    #Vraag koop stukje
    while vraag == True and moneyInAccount == 200:
            vraag1 = input("WAT KIES JIJ?\nKOOP/SPAREN/GELD\n")
            if vraag1 == "KOOP":
                    print("Je wilt dus gaan kopen kom maar winkelen")
                    winkel = True
                    vraag = False
            elif vraag1 == "SPAREN":
                    print("Je wilt dus gaan sparen")
                    sparen = True
                    vraag = False
            elif vraag1 == "GELD":
                    print("JE HEBT",inkomen,"EURO IN JE ZAK")
            else:
                print("GEEN ANTWOORD")


    
    #winkel text
    while winkel == True:
            print("WAT WIL JE KOPEN?")
            print("AUTO 1000 EURO")
            print("HUIS 65000 EURO")
            print("TELEFOON 600 EURO")
            print("KIES AUTO/HUIS/TELEFOON")
            koop = input()
            if koop == "AUTO" and inkomen > 1000:
                    print("JE HEBT EEN AUTO GEKOCHT")
                    print("JE GAAT TERUG NAAR MENU")
                    winkel = False
                    vraag = True
            elif koop == "HUIS" and inkomen > 65000:
                    print("JE HEBT EEN HUIS GEKOCHT")
                    print("JE GAAT TERUG NAAR MENU")
                    winkel = False
                    vraag = True
            elif koop == "TELEFOON" and inkomen > 600:
                    print("JE HEBT EEN TELEFOON GEKOCHT")
                    print("JE GAAT TERUG NAAR MENU")
                    winkel = False
                    vraag = True
            else:
                print("GEEN ANTWOORD OF GE HEBT GEEN GELD GA SPAREN")
                sparen = True
                winkel = False

    #sparen 
    while sparen == True:
            print("JE GAAT WERKEN BIJ APPIE")
            print("HOEVEEL UUR WIL JE WERKEN")
            uur = int(input())
            peruur = 6
            uur1 = uur * peruur
            print("Je moet een aantal seconden wachten.\nhoe meer je werkt hoelanger het duurt.")
            sleep(uur1 / 3)
            print("Je hebt",uur," uur gewerkt bij appie en je kreeg",uur1)
            inkomen += uur1
            vraag = True
            sparen = False

