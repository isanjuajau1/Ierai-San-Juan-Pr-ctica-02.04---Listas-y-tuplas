#Escribir un programa que pida al usuario una palabra y muestre por pantalla el 
# número de veces que contiene cada vocal.

p = input('Escribe una palabra: ')
p = p.lower()
listap = list(p)
vocal_a = 0
vocal_e = 0
vocal_i = 0
vocal_o = 0
vocal_u = 0


for i in range(len(listap)):
    if listap[i] == 'a':
        vocal_a += 1
    elif listap[i] == 'e':
        vocal_e += 1
    elif listap[i] == 'i':
        vocal_i += 1
    elif listap[i] == 'o':
        vocal_o += 1
    elif listap[i] == 'u':
        vocal_u += 1

print('{} tiene la vocal "A" {} veces, la vocal "E" {} veces, la vocal "I" {} veces, la vocal "O" {} veces y la vocal "U" {} veces. '.format(p,vocal_a, vocal_e, vocal_i, vocal_o, vocal_u ))