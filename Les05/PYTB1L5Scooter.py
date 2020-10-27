verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2


def bereken_maandkosten(km_per_maand):
    maandkosten = (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter + verzekering_per_maand)
    print("Je kosten zijn € " + str(maandkosten))

km_per_maand = ""

while not isinstance(km_per_maand, float):

    # probeer of deze code werkt    
    try:
        # Vraag om een getal en sla op in de variabele: invoer
        km_per_maand = input("Hoveel km rij je per maand?: ")
        
        # Probeer de input om te zetten in een float (getal met cijfers achter de komma)
        km_per_maand = float(km_per_maand)

        # Als Python tot hier komt dan is het gelukt! Anders wordt de except code uitgevoerd
        bereken_maandkosten(km_per_maand)

    except ValueError:
        # Als er een ValueError optreedt, dan voer je deze code uit 
        print(km_per_maand + " is geen geldig getal!")


