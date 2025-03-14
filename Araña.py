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
dpata2up=cylinder(pos=vector(2.4,-0.8,0.6),axis=vector(0.8,1.1,0.5),radius=0.1,color=color.yellow)
drodilla2=sphere(pos=vector(3.2,0.3,1.1),radius=0.11,color=color.cyan)
dpata2down=cylinder(pos=vector(3.2,0.3,1.1),radius=0.1,color=color.yellow)

#Pata 2 izquierda
ipata2up=cylinder(pos=vector(2.4,-0.8,-0.6),axis=vector(0.8,1.1,-0.5),radius=0.1,color=color.yellow)
irodilla2=sphere(pos=vector(3.2,0.3,-1.1),radius=0.11,color=color.cyan)
ipata2down=cylinder(pos=vector(3.2,0.3,-1.1),radius=0.1,color=color.yellow)

#Pata 3 derecha
dpata3up=cylinder(pos=vector(2.3,-0.6,0.7),axis=vector(0.3,1.3,0.4),radius=0.1,color=color.yellow)
drodilla3=sphere(pos=vector(2.6,0.7,1.1),radius=0.11,color=color.cyan)
dpata3down=cylinder(pos=vector(2.6,0.7,1.1),radius=0.1,color=color.yellow)

#Pata 3 izquieda
ipata3up=cylinder(pos=vector(2.3,-0.6,-0.7),axis=vector(0.3,1.3,-0.4),radius=0.1,color=color.yellow)
irodilla3=sphere(pos=vector(2.6,0.7,-1.1),radius=0.11,color=color.cyan)
ipata3down=cylinder(pos=vector(2.6,0.7,-1.1),radius=0.1,color=color.yellow)

#Pata 4 derecha
dpata4up=cylinder(pos=vector(1.9,-0.6,0.6),axis=vector(0.2,1.3,0.4),radius=0.1,color=color.yellow)
drodilla4=sphere(pos=vector(2.1,0.7,1),radius=0.11,color=color.cyan)
dpata4down=cylinder(pos=vector(2.1,0.7,1),radius=0.1,color=color.yellow)

#Pata 4 izquieda
ipata4up=cylinder(pos=vector(1.9,-0.6,-0.6),axis=vector(0.2,1.3,-0.4),radius=0.1,color=color.yellow)
irodilla4=sphere(pos=vector(2.1,0.7,-1),radius=0.11,color=color.cyan)
ipata4down=cylinder(pos=vector(2.1,0.7,-1),radius=0.1,color=color.yellow)

#Ojos derecha
dojo1=sphere(pos=vector(2.8,-1.2,0.15),radius=0.25,color=color.green)
dojo2=sphere(pos=vector(2.8,-1.2,0.4),radius=0.15,color=color.magenta)

#Ojos izquierda
iojo1=sphere(pos=vector(2.8,-1.2,-0.15),radius=0.25,color=color.green)
iojo2=sphere(pos=vector(2.8,-1.2,-0.4),radius=0.15,color=color.magenta)

#Comillos
dcomillo=cone(pos=vector(2.8,-1.5,0.16),axis=vector(0,-0.25,0.1),radius=0.1,color=color.cyan)
icomillo=cone(pos=vector(2.8,-1.5,-0.16),axis=vector(0,-0.25,-0.1),radius=0.1,color=color.cyan)


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
    dpata1down.axis = vector(0, -2, 0.8)
    ipata1down.axis = vector(0, -2,-0.8)
    dpata2down.axis = vector(0, -2, 1)
    ipata2down.axis = vector(0, -2,-1)
    dpata3down.axis = vector(0, -2, 1.1)
    ipata3down.axis = vector(0, -2,-1.1)
    dpata4down.axis = vector(0, -2, 0.8)
    ipata4down.axis = vector(0, -2,-0.8)
    dpata1down.rotate(angle=math.radians(angulo), axis=vector(1, -1.5, 2.5), origin=dpata1down.pos)
    ipata1down.rotate(angle=math.radians(angulo2), axis=vector(1, 1.5, -2.5), origin=ipata1down.pos)
    dpata2down.rotate(angle=math.radians(angulo2), axis=vector(1, 1.5, -2.5), origin=dpata2down.pos)
    ipata2down.rotate(angle=math.radians(angulo), axis=vector(1, -1.5, 2.5), origin=ipata2down.pos)
    dpata3down.rotate(angle=math.radians(angulo2), axis=vector(1, -1.5, 2.5), origin=dpata3down.pos)
    ipata3down.rotate(angle=math.radians(angulo), axis=vector(1, 1.5, -2.5), origin=ipata3down.pos)
    dpata4down.rotate(angle=math.radians(angulo2), axis=vector(1, 1.5, -2.5), origin=dpata4down.pos)
    ipata4down.rotate(angle=math.radians(angulo), axis=vector(1, -1.5, 2.5), origin=ipata4down.pos)
    
    tiempo += 0.1
    tiempo2 -= 0.1
    