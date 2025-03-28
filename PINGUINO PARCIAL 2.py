from vpython import *
#from three import *
import math

# Crear la escena
titulo = canvas(title="\t\t\tPinguino")
#scene.background = new THREE.Color('orange');

# Cabeza del pingüino
cabeza = sphere(color=color.cyan, pos=vector(0,8,0), radius=7)

# Ojos
ojo1 = sphere(color=color.yellow, pos=vector(-4,7,5), radius=2.5)
ojo2 = sphere(color=color.yellow, pos=vector(4,7,5), radius=2.5)

# Pico del pingüino
pico = cylinder(color=color.yellow, pos=vector(-0.3,5,7.5))
pico.radius1 = 3  # base del cono
pico.radius2 = 0  # punta del cono

# Cuerpo del pingüino
cuerpo1 = sphere(color=color.cyan, pos=vector(0,-5 ,0), radius=10)
cuerpo2 = sphere(color=color.white, pos=vector(0,-5.7,5), radius=7)

# Alas (esferas aplanadas)
ala_izquierda = ellipsoid(color=color.cyan, pos=vector(-10,-4,2), length=14, height=2, width=7)
ala_derecha = ellipsoid(color=color.cyan, pos=vector(10,-4,2), length=14, height=2, width=7)

# Patas (cilindros)
pata_izquierda = cylinder(pos=vector(-3,-16,2), axis=vector(0, 1, 0), radius=2.5, length=10, color=color.orange)
pata_derecha = cylinder(pos=vector(3,-16,2), axis=vector(0, 1, 0), radius=2.5, length=10, color=color.orange)

# Colocar las alas, las patas, los ojos y el pico como hijos del cuerpo
ala_izquierda.pos = cuerpo1.pos + vector(-10,1,2)
ala_derecha.pos = cuerpo1.pos + vector(10,1,2)

pata_izquierda.pos = cuerpo1.pos + vector(-3,-11,2)
pata_derecha.pos = cuerpo1.pos + vector(3,-11,2)

ojo1.pos = cabeza.pos + vector(-4,7,5)
ojo2.pos = cabeza.pos + vector(4,7,5)

pico.pos = cabeza.pos + vector(-0.3,5,7.5)

# Parámetros para la animación
amplitud = 25  # Ángulo máximo de inclinación
frecuencia = 0.1  # Control de la velocidad del balanceo
tiempo = 0
radio = 20  # Radio de la trayectoria circular
velocidad_angular = 0.01  # Velocidad de avance en el círculo
angulo_circular = 0  # Ángulo de movimiento circular

while True:
    rate(30)  # Controla la velocidad de la animación
    
    # El movimiento circular sobre el eje XZ (horizontal)
    angulo = amplitud * math.sin(frecuencia * tiempo)
    angulo_circular += velocidad_angular
    cabeza.pos = vector(radio * math.cos(angulo_circular), 8, radio * math.sin(angulo_circular))
    cabeza.rotate(angle=math.radians(angulo), axis=vector(0,1,0), origin=cuerpo2.pos)
    cuerpo1.pos = vector(radio * math.cos(angulo_circular), -5, radio * math.sin(angulo_circular))
    cuerpo2.pos = vector(radio * math.cos(angulo_circular), -5.7, radio * math.sin(angulo_circular))

    # Movimiento de las alas
    ala_izquierda.pos = cuerpo1.pos + vector(10,0,2)
    ala_derecha.pos = cuerpo1.pos + vector(-10,0,2)
    ala_izquierda.rotate(angle=math.radians(angulo), axis=vector(0,1,0), origin=ala_izquierda.pos)
    ala_derecha.rotate(angle=math.radians(angulo), axis=vector(0,-1,0), origin=ala_derecha.pos)
    tiempo += 0.1
    
    # Movimiento de las patas (sincronizado con el cuerpo)
    pata_izquierda.pos = cuerpo1.pos + vector(-3,-11,2)
    pata_derecha.pos = cuerpo1.pos + vector(3,-11,2)
    pata_izquierda.rotate(angle=math.radians(angulo), axis=vector(0,1,0), origin=cuerpo1.pos)
    pata_derecha.rotate(angle=math.radians(angulo), axis=vector(0,1,0), origin=cuerpo1.pos)
    
    # Movimiento de los ojos
    ojo1.pos = cabeza.pos + vector(-4,2,4)
    ojo2.pos = cabeza.pos + vector(4,2,4)

    # Movimiento del pico
    pico.pos = cabeza.pos + vector(-0.3,0.7,7.5)
    
    # Actualizamos el tiempo
    tiempo += 1