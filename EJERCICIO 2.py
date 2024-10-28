'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por
pantalla el mensaje: Yo estudio <asignatura>, donde <asignatura> es cada una 
de las asignaturas de la lista.'''

asig = ['RETE', 'DAPI', 'SHID', 'GPIT', 'SIRC', 'SIPA']

for i in range(len(asig)):
    print('Yo estudio {}.'.format(asig[i]))