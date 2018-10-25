import numpy as np
from numpy.linalg import norm
from numpy import dot, sign
from random import uniform
from time import sleep

"""
TODO: Realizar Mediciones
TODO: Intentar animar
TODO: Mejorar Rendimiento
TODO: Insertar variacion de Volumen
"""

'''Defino mi particula'''
class Particula(object):
    def __init__(self, r, v, radius = 1, mass = 1):
        self.radius = radius
        self.mass = mass
        self.pos = np.array(r)
        self.vel = np.array(v)
        
    def __str__(self):
        r =  'r = (' + str(self.pos[0]) + ', ' + str(self.pos[1]) + ') \n'
        r+=  'v = (' + str(self.vel[0]) + ', ' + str(self.vel[1]) + ')'
        return r
    
    def get_r(self):
        return self.pos
    
    def get_v(self):
        return self.vel

''' Verifico colisiones en cada paso'''
def collide():
    # Check contra las paredes (por si se pasaron asi no se escapan)
    for part in part_list:
        if part.pos[0] >= dimA or part.pos[0] <= -dimA:
            part.vel[0] = -part.vel[0]
            part.pos[0] = dimA*sign(part.pos[0])
        elif part.pos[1] >= dimB or part.pos[1] <= -dimB:
            part.vel[1] = -part.vel[1]
            part.pos[1] = dimB*sign(part.pos[1])
        part.pos = part.pos + part.vel*step
        
    # Check contra las demas particulas
    for i, part1 in enumerate(part_list[:-1]):
        for part2 in part_list[i+1:]:
            if norm(part1.pos - part2.pos) <= 2:
                r = part1.pos - part2.pos #Saco direccion de choque
                r = r/norm(r) #Normalizo la direccion
                vi = dot(part1.vel, r) #Proyecto las velocidades a swapear
                vj = dot(part2.vel, r)
                change = vi - vj
                part1.vel = part1.vel - change*r
                part2.vel = part2.vel + change*r
                print('Colision')

''' INICIACION DE PARAMETROS '''
no_part = 100
dimA = 200
dimB = 100
step = 0.1
part_list = []

# Creo mis particulas
for i in range(no_part):
    part = Particula([uniform(-dimA, dimA), uniform(-dimB, dimB)],
                        [uniform(-1, 1), uniform(-1, 1)])
    part_list.append(part)
T=[]

# ATAQUENSE MALDITAS
for i in range(50):
    collide()
