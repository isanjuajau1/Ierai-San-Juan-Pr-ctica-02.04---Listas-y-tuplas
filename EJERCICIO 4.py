#Escribir un programa que pregunte al usuario los números ganadores de la 
#lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados 
#de menor a mayor.
loteria = []

for i in range(0,6):
    add = int(input('Escribe un número ganador de la lotería: '))
    loteria.insert(i, add)

loteria.sort()

print(loteria)