#Escribir un programa que pida al usuario una palabra y muestre por pantalla si 
#es un palíndromo.

p = input('Escribe una palabra: ')
q = p
plista = list(p) # plista = lista normal
plist = list(q)
plistr = plist.reverse() # plist = lista inversa
palindromo = False

if plista == plist:
    palindromo = True

if palindromo == True:
    print('La palabra {} es palíndroma. '.format(p))
else:
    print('La palabra {} no es palíndroma. '.format(p))