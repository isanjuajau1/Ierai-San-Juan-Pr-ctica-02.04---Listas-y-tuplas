#Escribir un programa que almacene el abecedario en una lista, elimine de la 
#lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la 
#lista resultante.
import string


abc = list(string.ascii_lowercase)


for i in range(len(abc), 1, -1):
    
    if i % 3 == 0:
        abc.pop(-i)

print(abc)