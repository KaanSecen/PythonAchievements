
#Deze functie zorgt voor de stutter
def stutter(word):
	return (3*(word[:2]+'... '))+word


woordteller = 0

zin = input("type het woord!")
woorden =zin.split(" ")

s = ' '


for woord in woorden:
	if len(woord) > 3:
		print(3*(woord[:2])+'... ' +woord)
	if len(woord) < 3:
		print(woord)