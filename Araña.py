from vpython import *
import math

panza=sphere(pos=vector(0,0,0),radius=1.5,size=vector(2,1,1),color=color.red)
cabeza=sphere(pos=vector(2,-1,0),radius=1,size=vector(2,1,1),color=color.blue)

#Pata 1 derecha
dpata1up=cylinder(pos=vector(2.1,-1,0.5),axis=vector(1.5,1,0.5),radius=0.1,color=color.yellow)
drodilla1=sphere(pos=vector(3.6,0,1),radius=0.11,color=color.cyan)
dpata1down=cylinder(pos=vector(3.6,0,1),radius=0.1,color=color.yellow)

#Pata 1 izquierda
ipata1up=cylinder(pos=vector(2.1,-1,-0.5),axis=vector(1.5,1,-0.5),radius=0.1,color=color.yellow)
irodilla1=sphere(pos=vector(3.6,0,-1),radius=0.11,color=color.cyan)
ipata1down=cylinder(pos=vector(3.6,0,-1),radius=0.1,color=color.yellow)

#Para 2 derecha
dpata2up=cylinder(pos=vector(2.2,-0.8,0.6),axis=vector(1,1,0.5),radius=0.1,color=color.yellow)
drodilla2=sphere(pos=vector(3.2,0.2,1.1),radius=0.11,color=color.cyan)
dpata2down=cylinder(pos=vector(3.2,0.2,1.1),radius=0.1,color=color.yellow)

#Pata 2 izquierda
ipata2up=cylinder(pos=vector(2.2,-0.8,-0.6),axis=vector(1,1,-0.5),radius=0.1,color=color.yellow)
irodilla2=sphere(pos=vector(3.2,0.2,-1.1),radius=0.11,color=color.cyan)
ipata2down=cylinder(pos=vector(3.2,0.2,-1.1),radius=0.1,color=color.yellow)

amplitud=20
amplitud2 = -20
tiempo=0
tiempo2=0
frecuencia=0.2
while True:
    rate (30)
    #dpata1down.rotate(angle=0.05,axis=vector(0,0,1))
    angulo = amplitud * math.sin(frecuencia * tiempo)
    angulo2 = amplitud2 * math.sin(frecuencia * tiempo2)
    dpata1down.axis = vector(0, -2, 1)
    ipata1down.axis = vector(0, -2,-1)
    dpata2down.axis = vector(0, -2, 1)
    ipata2down.axis = vector(0, -2,-1)
    dpata1down.rotate(angle=math.radians(angulo), axis=vector(1, -1.5, 2.5), origin=dpata1down.pos)
    ipata1down.rotate(angle=math.radians(angulo2), axis=vector(1, 1.5, -2.5), origin=ipata1down.pos)
    dpata2down.rotate(angle=math.radians(angulo2), axis=vector(1, 1.5, -2.5), origin=dpata2down.pos)
    ipata2down.rotate(angle=math.radians(angulo), axis=vector(1, -1.5, 2.5), origin=ipata2down.pos)
    tiempo += 0.1
    tiempo2 -= 0.1
    