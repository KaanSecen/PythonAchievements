Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is Kaan')
Mijn naam is Kaan
>>> naam = 'Kaan'
>>> print(naam)
Kaan
>>> print(naam.upper())

KAAN
>>> print(naam[0:2])
Ka
>>> print(naam[::-1])
naaK
>>> leeftijd = 17
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Kaan ben je al 17 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
18
>>> leeftijd-=1
>>> leeftijd
17
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
	    
SyntaxError: unexpected indent
>>>     print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
    
SyntaxError: unexpected indent
>>> elif leeftijd > 18:
	
SyntaxError: invalid syntax
>>>     print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
    
SyntaxError: unexpected indent
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
	hoelang_al18jaar = leeftijd - 18
	print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
	print('Je bent precies ' + str(leeftijd) + ' jaar')
from random import randint
SyntaxError: invalid syntax
>>> from random import randint
>>> randint(0,1000)
684
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
370
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 370
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-09 13:10:08.406342
>>> datum.strftime('%A %d %B %Y')
'Wednesday 09 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 09 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 09 settembre 2020'
>>> 