
#Deze functie zorgt voor de stutter
def stutter(word):
	return (3*(word[:2]+'... '))+word

word = input()
print(stutter(word))

input_woord = input("type het woord!")
lijst = input_woord.split(" ")

lijstshow = list(lijst)

print(lijstshow)

