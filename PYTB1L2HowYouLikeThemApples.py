import math

#Vervang de 0-en met de juiste berekeningen

trees               = 333             #hoeveel bomen zijn er in totaal?
shadedTrees         = math.ceil(222)  #hoeveel bomen staan er in de schaduw (afgerond naar boven)?
sunnyTrees          = 111             #hoeveel in de zon?

shadeOutputModifier = 80             #hoeveel procent productie geeft een schaduwboom?

sunnyTreeOutput     = 146             #hoeveel appels geeft 1 zonnige boom?
shadedTreeOutput    = 117             #hoeveel appels geeft 1 schaduw boom?

sunnyOutput         = 16206             #hoeveel appels geven alle zonnige bomen? 
shadedOutput        = 25794             #hoeveel appels geven alle schaduw bomen?
totalOutput         = 48438             #hoeveel appels zijn er in totaal?

owners              = 4             #met hoeveel mensen verdelen we de appels?

eatCount            = 6438             #hoeveel appels houden we over omdat ze niet eerlijk te verdelen zijn?
sellableOutput      = 42000             #hoeveel appels zijn er over en dus verkoopbaar?
cut                 = 10500             #hoeveel appels mag ik verkopen?


print("Amount sunny tree:",trees - shadedTrees)
print("Amount shadow tree:",trees - sunnyTrees)
print("Total Sunny tree Apples:",sunnyTrees * sunnyTreeOutput)
print("Total shadow tree Apples:",shadedTrees * shadedTreeOutput)
print("Total tree apples with eatable count",shadedOutput + sunnyOutput + 29 * 222)
print("Non eatable apples:", 29 * 222)
print("Sellable amount:",totalOutput - eatCount)
print("share by the people",sellableOutput / owners)
print("Final Amount",cut)