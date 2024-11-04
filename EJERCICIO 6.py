#Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al 
#usuario la nota que ha sacado en cada asignatura y elimine de la lista las 
#asignaturas aprobadas. Al final el programa debe mostrar por pantalla las
#asignaturas que el usuario tiene que repetir.

asig = ['RETE', 'DAPI', 'SHID', 'GPIT', 'SIRC', 'SIPA']
nota = []
asig_suspendidas = []


for i in range(len(asig)):
    pregunta = float(input('Cuanto has sacado en {}?: '.format(asig[i])))
    while (pregunta < 0) or (pregunta > 10):
        pregunta = float(input('Cuanto has sacado en {}? (Número del 0 al 10): '.format(asig[i])))
    
    if pregunta <5:
        asig_suspendidas.append(asig[i])



print('Tienes que recuperar', asig_suspendidas)