

tekstnamen = 'De Python lessen worden gegeven voor Erik, Erwin en ook door Hidde'
tekstvakken = 'SD vakken zijn Python, UXD, Frontend development en Backend development en nog veel meer ...'
tekstlast = 'Wat is hier het laatste woord?'
tekstzin = 'Het www is ontwikkeld vanaf 1989 door Tim Berners-Lee'

#Slicing voor de namen
Erik = tekstnamen[37:41]
Erwin = tekstnamen[43:48]
Hidde = tekstnamen[61:66]

#Sciling voor de vakken
python = tekstvakken[15:21]
UXD = tekstvakken[23:26]
Frontdev = tekstvakken[28:48]
BackDev = tekstvakken[52:72]

#Sclining voor de laaste woord
woordlast = tekstlast[24:30]

#Scling voor de tekst
eersteletter = tekstzin[5:7]
tweedeletter = tekstzin[29:32]
#Print Commands
print(Erik,Erwin,Hidde)
print(python,UXD,Frontdev,BackDev)
print(woordlast)
print(eersteletter,tweedeletter)
