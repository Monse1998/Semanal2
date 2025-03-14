from vpython import *
from time import *
import math

# Cabeza del pinguino
cabeza = sphere(color=color.cyan, pos=vector(0,8,0), radius=7)

# Ojos
ojo1 = sphere(color=color.yellow, pos=vector(-4,7,5), radius=2.5)
ojo2 = sphere(color=color.yellow, pos=vector(4,7,5), radius=2.5)

# Pico del pinguino
pico = cylinder(color=color.yellow, pos=vector(-0.3,5,7.5))
pico.radius1 = 3  # base del cono
pico.radius2 = 0  # punta del cono

# Cuerpo del pinguino
cuerpo1 = sphere(color=color.cyan, pos=vector(0,-5 ,0), radius=10)
cuerpo2 = sphere(color=color.white, pos=vector(0,-5.7,5), radius=7)

# Alas (esferas aplanadas)
ala_izquierda = ellipsoid(color=color.cyan, pos=vector(-10,-4,2), length=14, height=2, width=7)
ala_derecha = ellipsoid(color=color.cyan, pos=vector(10,-4,2), length=14, height=2, width=7)

# Patas (cilindros)
pata_izquierda = cylinder(pos=vector(-3,-16,2), axis=vector(0, 1, 0), radius=2.5, length=10, color=color.orange)
pata_derecha = cylinder(pos=vector(3,-16,2), axis=vector(0, 1, 0), radius=2.5, length=10, color=color.orange)

#Movimiento de alas y patas
amplitud = 25 #angulo maximo de inclinación
frecuencia = 0.1 #contro de la velocidad del balanceo
tiempo = 0
while True:
    rate(30)
    #el movimineto sera sobre x (balanceo hacia adelante y hacia atras)
    angulo = amplitud * math.sin(frecuencia * tiempo)
    
    #Alas
    ala_izquierda.rotate(angle=math.radians(angulo), axis=vector(0,1,0), origin=ala_izquierda.pos)
    ala_derecha.rotate(angle=math.radians(angulo), axis=vector(0,-1,0), origin=ala_derecha.pos)
    tiempo += 0.1
    
    #Patas
    pata_izquierda.axis=vector(0,6,0)
    pata_izquierda.rotate(angle=math.radians(angulo), axis=vector(1,0,0), origin=pata_izquierda.pos)
    pata_derecha.axis=vector(0,6,0)
    pata_derecha.rotate(angle=math.radians(angulo), axis=vector(-1,0,0), origin=pata_derecha.pos)
    tiempo += 0.1
