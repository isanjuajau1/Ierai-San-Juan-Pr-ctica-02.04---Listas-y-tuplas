#Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al 
#usuario la nota que ha sacado en cada asignatura, y después las muestre por 
#pantalla con el mensaje En <asignatura> has sacado <nota> donde 
#<asignatura> es cada una des las asignaturas de la lista y <nota> cada una de 
#las correspondientes notas introducidas por el usuario.

asig = ['RETE', 'DAPI', 'SHID', 'GPIT', 'SIRC', 'SIPA']
nota = []

for i in range(len(asig)):
    pregunta = float(input('Cuanto has sacado en {}?: '.format(asig[i])))
    while (pregunta < 0) or (pregunta > 10):
        pregunta = float(input('Cuanto has sacado en {}? (Número del 0 al 10): '.format(asig[i])))

    nota.insert(i, pregunta)

print()

for j in range(len(asig)):
    print('En {} has sacado un {}.'.format(asig[j],nota[j]))

