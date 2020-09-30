print("Je loopt op straat en iemand komt per ongeluk tegen jou aan.")
print("WAT DOE JE?")

keuze1 = input("KIES: SORRY, VECHT OF BOOS\n>")

normaal = 0

if keuze1 == "SORRY":
    print("JE ZEGT SORRY TEGEN HEM!")
    print("HIJ ZEGT: HIJ ZEGT SORRY WAS MIJN FOUT.\n\n")
    normaal =+ 20
    print(normaal)
elif keuze1 == "VECHT":
    print("JE VECHT TEGEN HEM!")
    print("JE HEBT VERLOREN TEGEN HEM!\nJE LOOPT WEG MET EEN BLOEDNEUS WEG!")
elif keuze1 == "BOOS":
    print("JE BENT BOOS TEGEN HEM")
    print("HIJ ZEGT: WAAROM BEN JE ZO BOOS!\nHET WAS PER ONGELUK.")
else:
    print("GEEN ANTWOORD ONTVANGEN")


print("Je loopt binnen een supermarkt.\nJe ziet iemand vechten doe je mee?")
keuze2 = input("KIES: NEE OF JAn>")

if keuze2 == "JA":
    print("JE GAAT VECHTEN")
    print("JE HEBT EEN WINKELVERBOD GEKREGEN!!!")
elif keuze2 == "NEE":
    print("JE GAAT VERDER WINKELEN")
    normaal =+ 20
else:
    print("JE MOET CAPS GEBRUIKEN")
    
print("Je loopt terug naar huis iemand loopt heletijd achter jou.\nGA JE VECHTEN JA OF NEE?")

keuze3 = input("KIES: NEE OF JAn>")

if keuze3 == "JA":
    print("JE GAAT VECHTEN")
    print("HIJ HEEFT JOU EEN KLAP OP JOU HOOFD GEGEVEN")
elif keuze3 == "NEE":
    print("JE LOOPT VERDER NAAR HUIS")
    normaal =+ 20
else:
    print("JE MOET CAPS GEBRUIKEN")
    
print("IEMAND KOMT OP BEZOEK.\nGA JE VECHTEN JA OF NEE?")

keuze4 = input("KIES: NEE OF JAn>")

if keuze4 == "JA":
    print("JE GAAT VECHTEN")
    print("HIJ ZEGT IK KOM NOOIT MEER OP BEZOEK")
elif keuze4 == "NEE":
    print("JE GAAT PRATEN MET ELKAAR")
    normaal =+ 20
else:
    print("JE MOET CAPS GEBRUIKEN")

print("JE BUREN BRENGEN KOEKJES VOOR JOU\nGA JE VECHTEN JA OF NEE?")

keuze4 = input("KIES: NEE OF JAn>")

if keuze4 == "JA":
    print("JE GAAT VECHTEN")
    print("DE BUREN SLAAN JE KAPOT")
elif keuze4 == "NEE":
    print("JE ZEGT DANKJEWEL EN JE PAKT DE KOEKJES YUMMMM")
    normaal =+ 20
else:
    print("JE MOET CAPS GEBRUIKEN")

print("EEN POLITIE AGENT LOOPT NAAST JOU\nGA JE VECHTEN JA OF NEE?")

keuze5 = input("KIES: NEE OF JAn>")

if keuze5 == "JA":
    print("JE GAAT VECHTEN")
    print("JE ZIT IN DE GEVANGENIS")
elif keuze5 == "NEE":
    print("JE LOOPT VERDER")
    normaal =+ 20
else:
    print("JE MOET CAPS GEBRUIKEN")

print("Je bent",normaal,"% Normaal Goedzo")




 