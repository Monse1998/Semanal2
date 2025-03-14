#ARAÑA

from vpython import *
import math

titulo=canvas(title="\t\tAraña")
panza=sphere(pos=vector(0,0,0),radius=1.5,size=vector(2,1,1),color=color.red)
cabeza=sphere(pos=vector(2,-1,0),radius=1,size=vector(2,1,1),color=color.blue)

#Pata 1 derecha
dpata1up=cylinder(pos=vector(2.1,-1,0.5),axis=vector(1.5,1,0.5),radius=0.1,color=color.gray(0.5))
drodilla1=sphere(pos=vector(3.6,0,1),radius=0.11,color=color.black)
dpata1down=cylinder(pos=vector(3.6,0,1),radius=0.1,color=color.gray(0.5))

#Pata 1 izquierda
ipata1up=cylinder(pos=vector(2.1,-1,-0.5),axis=vector(1.5,1,-0.5),radius=0.1,color=color.gray(0.5))
irodilla1=sphere(pos=vector(3.6,0,-1),radius=0.11,color=color.black)
ipata1down=cylinder(pos=vector(3.6,0,-1),radius=0.1,color=color.gray(0.5))

#Para 2 derecha
dpata2up=cylinder(pos=vector(2.4,-0.8,0.6),axis=vector(0.8,1.1,0.5),radius=0.1,color=color.gray(0.5))
drodilla2=sphere(pos=vector(3.2,0.3,1.1),radius=0.11,color=color.black)
dpata2down=cylinder(pos=vector(3.2,0.3,1.1),radius=0.1,color=color.gray(0.5))

#Pata 2 izquierda
ipata2up=cylinder(pos=vector(2.4,-0.8,-0.6),axis=vector(0.8,1.1,-0.5),radius=0.1,color=color.gray(0.5))
irodilla2=sphere(pos=vector(3.2,0.3,-1.1),radius=0.11,color=color.black)
ipata2down=cylinder(pos=vector(3.2,0.3,-1.1),radius=0.1,color=color.gray(0.5))

#Pata 3 derecha
dpata3up=cylinder(pos=vector(2.3,-0.6,0.7),axis=vector(0.3,1.3,0.4),radius=0.1,color=color.gray(0.5))
drodilla3=sphere(pos=vector(2.6,0.7,1.1),radius=0.11,color=color.black)
dpata3down=cylinder(pos=vector(2.6,0.7,1.1),radius=0.1,color=color.gray(0.5))

#Pata 3 izquieda
ipata3up=cylinder(pos=vector(2.3,-0.6,-0.7),axis=vector(0.3,1.3,-0.4),radius=0.1,color=color.gray(0.5))
irodilla3=sphere(pos=vector(2.6,0.7,-1.1),radius=0.11,color=color.black)
ipata3down=cylinder(pos=vector(2.6,0.7,-1.1),radius=0.1,color=color.gray(0.5))

#Pata 4 derecha
dpata4up=cylinder(pos=vector(1.9,-0.6,0.6),axis=vector(0.2,1.3,0.4),radius=0.1,color=color.gray(0.5))
drodilla4=sphere(pos=vector(2.1,0.7,1),radius=0.11,color=color.black)
dpata4down=cylinder(pos=vector(2.1,0.7,1),radius=0.1,color=color.gray(0.5))

#Pata 4 izquieda
ipata4up=cylinder(pos=vector(1.9,-0.6,-0.6),axis=vector(0.2,1.3,-0.4),radius=0.1,color=color.gray(0.5))
irodilla4=sphere(pos=vector(2.1,0.7,-1),radius=0.11,color=color.black)
ipata4down=cylinder(pos=vector(2.1,0.7,-1),radius=0.1,color=color.gray(0.5))

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
frecuencia=0.5

#ROBOT 

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

#PINGUINO

from vpython import *
import math

titulo = canvas(title="\t\t\tPinguino")

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

#Movimiento Monse
amplitud = 23
amplitud2 = -23
frecuencia = 0.2
tiempom=0
tiempom2=0
#Movimiento Moy
tiempo = 0
tiempo2 = 0
tiempo3=0
tiempo4=0
#Movimiento Sebas
tiempos=0
while True:
    rate(40)  
    
    #dpata1down.rotate(angle=0.05,axis=vector(0,0,1))
    angulom = amplitud * math.sin(frecuencia * tiempom)
    angulom2 = amplitud2 * math.sin(frecuencia * tiempom2)
    dpata1down.axis = vector(0, -2, 0.8)
    ipata1down.axis = vector(0, -2,-0.8)
    dpata2down.axis = vector(0, -2, 1)
    ipata2down.axis = vector(0, -2,-1)
    dpata3down.axis = vector(0, -2, 1.1)
    ipata3down.axis = vector(0, -2,-1.1)
    dpata4down.axis = vector(0, -2, 0.8)
    ipata4down.axis = vector(0, -2,-0.8)
    dpata1down.rotate(angle=math.radians(angulom), axis=vector(1, -1.5, 2.5), origin=dpata1down.pos)
    ipata1down.rotate(angle=math.radians(angulom2), axis=vector(1, 1.5, -2.5), origin=ipata1down.pos)
    dpata2down.rotate(angle=math.radians(angulom2), axis=vector(1, 1.5, -2.5), origin=dpata2down.pos)
    ipata2down.rotate(angle=math.radians(angulom), axis=vector(1, -1.5, 2.5), origin=ipata2down.pos)
    dpata3down.rotate(angle=math.radians(angulom2), axis=vector(1, -1.5, 2.5), origin=dpata3down.pos)
    ipata3down.rotate(angle=math.radians(angulom), axis=vector(1, 1.5, -2.5), origin=ipata3down.pos)
    dpata4down.rotate(angle=math.radians(angulom2), axis=vector(1, 1.5, -2.5), origin=dpata4down.pos)
    ipata4down.rotate(angle=math.radians(angulom), axis=vector(1, -1.5, 2.5), origin=ipata4down.pos)
    
    tiempom += 0.1
    tiempom2 -= 0.1
    
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
    
    #el movimineto sera sobre x (balanceo hacia adelante y hacia atras)
    angulos = amplitud * math.sin(frecuencia * tiempos)
    
    #Alas
    ala_izquierda.rotate(angle=math.radians(angulos), axis=vector(0,1,0), origin=ala_izquierda.pos)
    ala_derecha.rotate(angle=math.radians(angulos), axis=vector(0,-1,0), origin=ala_derecha.pos)
    tiempos += 0.1
    
    #Patas
    pata_izquierda.axis=vector(0,6,0)
    pata_izquierda.rotate(angle=math.radians(angulos), axis=vector(1,0,0), origin=pata_izquierda.pos)
    pata_derecha.axis=vector(0,6,0)
    pata_derecha.rotate(angle=math.radians(angulos), axis=vector(-1,0,0), origin=pata_derecha.pos)
    tiempos += 0.1