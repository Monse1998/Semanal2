from vpython import *
import math


titulo = canvas(title="\t\t\tROBOT")


cubo = box(pos=vector(-12, 6, 0), size=vector(2, 2, 2), color=color.gray(0.5))
cubo2 = box(pos=vector(-12, 10, 0), size=vector(6, 6, 6), color=color.gray(0.5))
cubo3 = box(pos=vector(-8, 10, 0), size=vector(2, 2, 2), color=color.gray(0.5))
cubo4 = box(pos=vector(-16, 10, 0), size=vector(2, 2, 2), color=color.gray(0.5))
cubo5 = box(pos=vector(-12, 2, 0), size=vector(6, 6, 6), color=color.gray(0.5))
cubo6 = box(pos=vector(-12, 2, 0), size=vector(6, 6, 6), color=color.gray(0.5))
cubo7 = box(pos=vector(-14, 10, 3), size=vector(2, 2, 2), color=color.white)
cubo6 = box(pos=vector(-10, 10, 3), size=vector(2, 2, 2), color=color.white)
cili1 = cylinder(pos=vector(-8, -3, 0), axis=vector(0, 6, 0), radius=1, color=color.gray(0.5))
cili2 = cylinder(pos=vector(-16, -3, 0), axis=vector(0, 6, 0), radius=1, color=color.gray(0.5))
cili3 = cylinder(pos=vector(-10, -6, 0), axis=vector(0, 6, 0), radius=1, color=color.gray(0.5))
cili4 = cylinder(pos=vector(-14, -6, 0), axis=vector(0, 6, 0), radius=1, color=color.gray(0.5))
cili5 = cylinder(pos=vector(-10, 12, 0), axis=vector(0, 3, 0), radius=1, color=color.gray(0.5))
cili6 = cylinder(pos=vector(-14, 12, 0), axis=vector(0, 3, 0), radius=1, color=color.gray(0.5))
cubo8 =box(pos=vector(-12, 2, -3), size=vector(5, 5, 5), color=color.gray(0.5))
cili6 = cylinder(pos=vector(-13, 4, -4), axis=vector(0, 3, 0), radius=1, color=color.cyan)
cili6 = cylinder(pos=vector(-11, 4, -4), axis=vector(0, 3, 0), radius=1, color=color.cyan)




amplitud = 23
amplitud2 = -23
frecuencia = 0.2
tiempo = 0
tiempo2 = 0
tiempo3=0
tiempo4=0
while True:
    rate(40)  
    
    
    cili1.rotate(angle=0.05, axis=vector(0, 0, 1))
    cili2.rotate(angle=0.05, axis=vector(0, 0, 1))
    cili3.rotate(angle=0.05, axis=vector(0, 0, 1))
    cili4.rotate(angle=0.05, axis=vector(0, 0, 1))
    
    
    angulo = amplitud * math.sin(frecuencia * tiempo)
    cili1.axis = vector(0, 6, 0)
    cili1.rotate(angle=math.radians(angulo), axis=vector(1, 0, 0), origin=cili1.pos)
    tiempo += 0.1  
    
    angulo2 = amplitud2 * math.sin(frecuencia * tiempo2)
    cili2.axis = vector(0, 6, 0)
    cili2.rotate(angle=math.radians(angulo2), axis=vector(1, 0, 0), origin=cili2.pos)
    tiempo2 += 0.1
    
    angulo = amplitud * math.sin(frecuencia * tiempo4)
    cili4.axis = vector(0, 6, 0)
    cili4.rotate(angle=math.radians(angulo), axis=vector(1, 0, 0), origin=cili4.pos)
    tiempo3 += 0.1  
    
    angulo2 = amplitud2 * math.sin(frecuencia * tiempo3)
    cili3.axis = vector(0, 6, 0)
    cili3.rotate(angle=math.radians(angulo2), axis=vector(1, 0, 0), origin=cili3.pos)
    tiempo4+= 0.1  